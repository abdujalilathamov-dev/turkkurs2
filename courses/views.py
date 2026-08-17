import random

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import RegisterForm
from .models import Certificate, ExamAttempt, Lesson, LessonCompletion, Level, Question
from .progress import (
    get_certificate, get_completed_lessons_count, get_overall_progress_percent,
    get_total_lessons, has_certificate, is_eligible_for_exam,
)

LESSON_PASS_PERCENT = 60
EXAM_PASS_PERCENT = 70
EXAM_QUESTION_COUNT = 15


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Xush kelibsiz, {user.username}! Turk tilini o'rganishni boshlaymiz.")
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def dashboard(request):
    levels = Level.objects.filter(is_active=True).prefetch_related('darslar')
    completed_ids = set(
        LessonCompletion.objects.filter(user=request.user).values_list('lesson_id', flat=True)
    )

    levels_data = []
    for level in levels:
        lessons = level.darslar.filter(is_active=True)
        levels_data.append({
            'level': level,
            'lessons': lessons,
            'total': lessons.count(),
            'done': sum(1 for l in lessons if l.id in completed_ids),
        })

    context = {
        'levels_data': levels_data,
        'completed_ids': completed_ids,
        'progress_percent': get_overall_progress_percent(request.user),
        'completed_count': get_completed_lessons_count(request.user),
        'total_lessons': get_total_lessons(),
        'exam_eligible': is_eligible_for_exam(request.user),
        'has_certificate': has_certificate(request.user),
        'certificate': get_certificate(request.user),
    }
    return render(request, 'courses/dashboard.html', context)


@login_required
def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk, is_active=True)
    completion = LessonCompletion.objects.filter(user=request.user, lesson=lesson).first()
    context = {
        'lesson': lesson,
        'vocabulary': lesson.lugat.all(),
        'completion': completion,
        'question_count': lesson.question_count,
    }
    return render(request, 'courses/lesson_detail.html', context)


@login_required
def lesson_test(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk, is_active=True)
    questions = list(lesson.savollar.all())

    if not questions:
        messages.info(request, "Bu darsda hozircha test savollari yo'q.")
        return redirect('lesson_detail', pk=lesson.pk)

    if request.method == 'POST':
        correct = 0
        results = []
        for q in questions:
            chosen = request.POST.get(f'q{q.id}')
            is_correct = chosen == q.correct_option
            if is_correct:
                correct += 1
            results.append({'question': q, 'chosen': chosen, 'is_correct': is_correct})

        percent = round((correct / len(questions)) * 100)
        passed = percent >= LESSON_PASS_PERCENT

        if passed:
            completion, created = LessonCompletion.objects.get_or_create(
                user=request.user, lesson=lesson,
                defaults={'best_score_percent': percent, 'attempts': 1},
            )
            if not created:
                completion.attempts += 1
                completion.best_score_percent = max(completion.best_score_percent, percent)
                completion.save()

        context = {
            'lesson': lesson, 'results': results, 'correct': correct,
            'total': len(questions), 'percent': percent, 'passed': passed,
            'pass_threshold': LESSON_PASS_PERCENT,
        }
        return render(request, 'courses/lesson_test_result.html', context)

    context = {'lesson': lesson, 'questions': questions}
    return render(request, 'courses/lesson_test.html', context)


@login_required
def exam_info(request):
    context = {
        'eligible': is_eligible_for_exam(request.user),
        'progress_percent': get_overall_progress_percent(request.user),
        'completed_count': get_completed_lessons_count(request.user),
        'total_lessons': get_total_lessons(),
        'has_certificate': has_certificate(request.user),
        'certificate': get_certificate(request.user),
        'exam_pool_count': Question.objects.filter(lesson__isnull=True).count(),
        'pass_threshold': EXAM_PASS_PERCENT,
        'question_count': EXAM_QUESTION_COUNT,
    }
    return render(request, 'courses/exam_info.html', context)


@login_required
def exam_take(request):
    if not is_eligible_for_exam(request.user):
        messages.warning(request, "Imtihonga kirishdan oldin barcha darslarni tugatishingiz kerak.")
        return redirect('exam_info')

    pool = list(Question.objects.filter(lesson__isnull=True))
    if len(pool) < 5:
        messages.info(request, "Hozircha imtihon savollari yetarli emas. Keyinroq urinib ko'ring.")
        return redirect('exam_info')

    if request.method == 'POST':
        question_ids = [int(qid) for qid in request.POST.getlist('question_ids')]
        questions = list(Question.objects.filter(id__in=question_ids))
        correct = 0
        results = []
        for q in questions:
            chosen = request.POST.get(f'q{q.id}')
            is_correct = chosen == q.correct_option
            if is_correct:
                correct += 1
            results.append({'question': q, 'chosen': chosen, 'is_correct': is_correct})

        total = len(questions)
        percent = round((correct / total) * 100) if total else 0
        passed = percent >= EXAM_PASS_PERCENT

        attempt = ExamAttempt.objects.create(
            user=request.user, score=correct, total=total, percent=percent, passed=passed,
        )

        certificate = None
        if passed and not has_certificate(request.user):
            certificate = Certificate.objects.create(user=request.user, exam_attempt=attempt)
        elif passed:
            certificate = get_certificate(request.user)

        context = {
            'attempt': attempt, 'results': results, 'percent': percent,
            'passed': passed, 'certificate': certificate, 'pass_threshold': EXAM_PASS_PERCENT,
        }
        return render(request, 'courses/exam_result.html', context)

    sample_size = min(EXAM_QUESTION_COUNT, len(pool))
    questions = random.sample(pool, sample_size)
    context = {'questions': questions}
    return render(request, 'courses/exam_take.html', context)


@login_required
def certificate_view(request, pk):
    certificate = get_object_or_404(Certificate, pk=pk, user=request.user)
    return render(request, 'courses/certificate.html', {'certificate': certificate})


def certificate_verify(request):
    certificate = None
    searched = False
    cert_no = request.GET.get('raqam', '').strip()
    if cert_no:
        searched = True
        certificate = Certificate.objects.filter(certificate_no__iexact=cert_no).first()
    return render(request, 'courses/certificate_verify.html', {
        'certificate': certificate, 'searched': searched, 'cert_no': cert_no,
    })


@login_required
def my_certificates(request):
    certificates = Certificate.objects.filter(user=request.user)
    return render(request, 'courses/my_certificates.html', {'certificates': certificates})


@login_required
def leaderboard(request):
    users = User.objects.filter(is_active=True)
    reyting = []
    for u in users:
        done = get_completed_lessons_count(u)
        if done <= 0:
            continue
        reyting.append({
            'user': u,
            'done': done,
            'progress': get_overall_progress_percent(u),
            'has_cert': has_certificate(u),
        })
    reyting.sort(key=lambda x: (x['has_cert'], x['done']), reverse=True)
    for i, row in enumerate(reyting, start=1):
        row['rank'] = i
    return render(request, 'courses/leaderboard.html', {'reyting': reyting[:50]})


@staff_member_required
def admin_dashboard(request):
    """Faqat admin/xodimlar uchun — chiroyli, umumiy statistikali boshqaruv paneli."""
    today = timezone.localdate()

    total_users = User.objects.count()
    today_registered = User.objects.filter(date_joined__date=today).count()

    active_today_ids = set()
    active_today_ids.update(
        LessonCompletion.objects.filter(completed_at__date=today).values_list('user_id', flat=True)
    )
    active_today_ids.update(
        ExamAttempt.objects.filter(taken_at__date=today).values_list('user_id', flat=True)
    )

    total_certificates = Certificate.objects.count()
    today_certificates = Certificate.objects.filter(issued_at__date=today).count()
    total_exam_attempts = ExamAttempt.objects.count()
    passed_attempts = ExamAttempt.objects.filter(passed=True).count()
    pass_rate = round((passed_attempts / total_exam_attempts) * 100) if total_exam_attempts else 0

    reyting = []
    for u in User.objects.all():
        reyting.append({
            'user': u,
            'done': get_completed_lessons_count(u),
            'progress': get_overall_progress_percent(u),
            'has_cert': has_certificate(u),
            'active_today': u.id in active_today_ids,
            'joined': u.date_joined,
        })
    reyting.sort(key=lambda x: (x['has_cert'], x['progress']), reverse=True)
    for i, row in enumerate(reyting, start=1):
        row['rank'] = i

    recent_registrations = User.objects.order_by('-date_joined')[:8]
    recent_certificates = Certificate.objects.select_related('user').order_by('-issued_at')[:8]

    context = {
        'total_users': total_users,
        'today_registered': today_registered,
        'active_today_count': len(active_today_ids),
        'total_certificates': total_certificates,
        'today_certificates': today_certificates,
        'pass_rate': pass_rate,
        'total_lessons': get_total_lessons(),
        'reyting': reyting,
        'recent_registrations': recent_registrations,
        'recent_certificates': recent_certificates,
        'today': today,
    }
    return render(request, 'courses/admin_dashboard.html', context)
