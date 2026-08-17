from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.models import User

from .models import Certificate, ExamAttempt, Lesson, LessonCompletion, Level, Question, VocabularyWord
from .progress import get_completed_lessons_count, get_overall_progress_percent, has_certificate


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'order', 'is_active', 'lesson_count']
    list_editable = ['order', 'is_active']
    search_fields = ['name', 'code']


class VocabularyInline(admin.TabularInline):
    model = VocabularyWord
    extra = 1


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    fields = ['text', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_option']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'level', 'order', 'question_count', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['level', 'is_active']
    search_fields = ['title', 'content']
    autocomplete_fields = ['level']
    inlines = [VocabularyInline, QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'lesson', 'correct_option']
    list_filter = ['lesson']
    search_fields = ['text']
    autocomplete_fields = ['lesson']


@admin.register(LessonCompletion)
class LessonCompletionAdmin(admin.ModelAdmin):
    list_display = ['user', 'lesson', 'best_score_percent', 'attempts', 'completed_at']
    list_filter = ['lesson__level']
    search_fields = ['user__username', 'lesson__title']
    autocomplete_fields = ['user', 'lesson']


@admin.register(ExamAttempt)
class ExamAttemptAdmin(admin.ModelAdmin):
    list_display = ['user', 'score', 'total', 'percent', 'passed', 'taken_at']
    list_filter = ['passed', 'taken_at']
    search_fields = ['user__username']
    autocomplete_fields = ['user']
    date_hierarchy = 'taken_at'


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['certificate_no', 'user', 'issued_at']
    search_fields = ['certificate_no', 'user__username']
    autocomplete_fields = ['user']
    readonly_fields = ['certificate_no']


class TurkKursUserAdmin(DefaultUserAdmin):
    """Standart User admin — progress va sertifikat holati qo'shilgan."""
    list_display = DefaultUserAdmin.list_display + (
        'tugatilgan_darslar', 'progress', 'sertifikat_bormi',
    )

    @admin.display(description="Tugatilgan darslar")
    def tugatilgan_darslar(self, obj):
        return get_completed_lessons_count(obj)

    @admin.display(description="Progress")
    def progress(self, obj):
        return f"{get_overall_progress_percent(obj)}%"

    @admin.display(description="Sertifikat", boolean=True)
    def sertifikat_bormi(self, obj):
        return has_certificate(obj)


admin.site.unregister(User)
admin.site.register(User, TurkKursUserAdmin)

admin.site.site_header = "Turk Tili Kursi — Boshqaruv paneli"
admin.site.site_title = "Turk Tili Kursi"
admin.site.index_title = "Xush kelibsiz"
