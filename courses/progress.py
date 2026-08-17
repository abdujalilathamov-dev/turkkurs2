from .models import Certificate, ExamAttempt, Lesson, LessonCompletion


def get_total_lessons() -> int:
    return Lesson.objects.filter(is_active=True).count()


def get_completed_lessons_count(user) -> int:
    return LessonCompletion.objects.filter(user=user).count()


def get_overall_progress_percent(user) -> int:
    total = get_total_lessons()
    if not total:
        return 0
    done = get_completed_lessons_count(user)
    return min(round((done / total) * 100), 100)


def is_eligible_for_exam(user) -> bool:
    """Foydalanuvchi barcha darslarni tugatgan bo'lsa, yakuniy imtihonga kirishi mumkin."""
    total = get_total_lessons()
    if not total:
        return False
    return get_completed_lessons_count(user) >= total


def get_best_exam_attempt(user):
    return ExamAttempt.objects.filter(user=user, passed=True).order_by('-percent').first()


def get_certificate(user):
    return Certificate.objects.filter(user=user).order_by('-issued_at').first()


def has_certificate(user) -> bool:
    return Certificate.objects.filter(user=user).exists()
