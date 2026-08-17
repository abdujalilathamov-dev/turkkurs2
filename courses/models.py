from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Level(models.Model):
    """Kurs darajasi — masalan Boshlang'ich (A1), O'rta (A2)."""
    name = models.CharField("Nomi", max_length=100)
    code = models.CharField("Kod (masalan A1)", max_length=10, blank=True)
    description = models.CharField("Qisqa tavsif", max_length=255, blank=True)
    order = models.PositiveIntegerField("Tartib raqami", default=0)
    is_active = models.BooleanField("Faol", default=True)

    class Meta:
        verbose_name = "Daraja"
        verbose_name_plural = "Darajalar"
        ordering = ['order']

    def __str__(self):
        return f"{self.name} ({self.code})" if self.code else self.name

    @property
    def lesson_count(self):
        return self.darslar.filter(is_active=True).count()


class Lesson(models.Model):
    """Bitta dars — mavzu, tushuntirish matni va lug'at bilan."""
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='darslar', verbose_name="Daraja")
    title = models.CharField("Sarlavha", max_length=200)
    content = models.TextField("Dars matni (tushuntirish)")
    video_url = models.URLField("Video havolasi (ixtiyoriy)", blank=True)
    order = models.PositiveIntegerField("Tartib raqami", default=0)
    is_active = models.BooleanField("Faol", default=True)
    created_at = models.DateTimeField("Qo'shilgan vaqt", auto_now_add=True)

    class Meta:
        verbose_name = "Dars"
        verbose_name_plural = "Darslar"
        ordering = ['level__order', 'order']

    def __str__(self):
        return f"{self.level.code} — {self.title}" if self.level.code else self.title

    def get_absolute_url(self):
        return reverse('lesson_detail', args=[self.pk])

    @property
    def question_count(self):
        return self.savollar.count()


class VocabularyWord(models.Model):
    """Dars ichidagi lug'at so'zi (turkcha — o'zbekcha)."""
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lugat', verbose_name="Dars")
    turkish = models.CharField("Turkcha so'z/ibora", max_length=150)
    uzbek = models.CharField("O'zbekcha ma'nosi", max_length=150)
    example = models.CharField("Misol gap (ixtiyoriy)", max_length=255, blank=True)
    order = models.PositiveIntegerField("Tartib", default=0)

    class Meta:
        verbose_name = "Lug'at so'zi"
        verbose_name_plural = "Lug'at so'zlari"
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.turkish} — {self.uzbek}"


class Question(models.Model):
    """Test savoli. Agar 'lesson' bo'sh bo'lsa — bu yakuniy imtihon savollari
    havzasiga tegishli (barcha darslardan umumlashtirilgan)."""

    class Variant(models.TextChoices):
        A = 'a', "A"
        B = 'b', "B"
        C = 'c', "C"
        D = 'd', "D"

    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, related_name='savollar', null=True, blank=True,
        verbose_name="Dars (bo'sh bo'lsa — yakuniy imtihon savoli)",
    )
    text = models.CharField("Savol matni", max_length=400)
    option_a = models.CharField("A varianti", max_length=200)
    option_b = models.CharField("B varianti", max_length=200)
    option_c = models.CharField("C varianti", max_length=200)
    option_d = models.CharField("D varianti", max_length=200)
    correct_option = models.CharField("To'g'ri javob", max_length=1, choices=Variant.choices)
    explanation = models.CharField("Tushuntirish (ixtiyoriy)", max_length=300, blank=True)

    class Meta:
        verbose_name = "Test savoli"
        verbose_name_plural = "Test savollari"

    def __str__(self):
        return self.text[:60]

    def options(self):
        return [
            ('a', self.option_a), ('b', self.option_b),
            ('c', self.option_c), ('d', self.option_d),
        ]


class LessonCompletion(models.Model):
    """Foydalanuvchi bitta darsni qanday natija bilan tugatgani."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tugatilgan_darslar',
        verbose_name="Foydalanuvchi",
    )
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='tugatganlar', verbose_name="Dars")
    best_score_percent = models.PositiveIntegerField("Eng yaxshi natija (%)", default=0)
    attempts = models.PositiveIntegerField("Urinishlar soni", default=0)
    completed_at = models.DateTimeField("Tugatilgan vaqt", auto_now=True)

    class Meta:
        verbose_name = "Dars natijasi"
        verbose_name_plural = "Dars natijalari"
        unique_together = ('user', 'lesson')

    def __str__(self):
        return f"{self.user.username} — {self.lesson.title} — {self.best_score_percent}%"


class ExamAttempt(models.Model):
    """Yakuniy imtihonga urinish."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='imtihon_urinishlari',
        verbose_name="Foydalanuvchi",
    )
    score = models.PositiveIntegerField("To'g'ri javoblar soni")
    total = models.PositiveIntegerField("Jami savollar soni")
    percent = models.PositiveIntegerField("Foiz natija")
    passed = models.BooleanField("O'tdi", default=False)
    taken_at = models.DateTimeField("Topshirilgan vaqt", auto_now_add=True)

    class Meta:
        verbose_name = "Imtihon urinishi"
        verbose_name_plural = "Imtihon urinishlari"
        ordering = ['-taken_at']

    def __str__(self):
        return f"{self.user.username} — {self.percent}% — {'O`tdi' if self.passed else 'O`tmadi'}"


class Certificate(models.Model):
    """Imtihondan muvaffaqiyatli o'tgan foydalanuvchiga beriladigan sertifikat."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sertifikatlar',
        verbose_name="Foydalanuvchi",
    )
    exam_attempt = models.OneToOneField(
        ExamAttempt, on_delete=models.CASCADE, related_name='sertifikat', verbose_name="Imtihon urinishi",
    )
    certificate_no = models.CharField("Sertifikat raqami", max_length=30, unique=True, blank=True)
    issued_at = models.DateTimeField("Berilgan sana", auto_now_add=True)

    class Meta:
        verbose_name = "Sertifikat"
        verbose_name_plural = "Sertifikatlar"
        ordering = ['-issued_at']

    def __str__(self):
        return f"{self.certificate_no} — {self.user.username}"

    def save(self, *args, **kwargs):
        if not self.certificate_no:
            year = timezone.localdate().year
            last = Certificate.objects.filter(certificate_no__startswith=f"TR-{year}-").order_by('-id').first()
            next_num = 1
            if last:
                try:
                    next_num = int(last.certificate_no.split('-')[-1]) + 1
                except (ValueError, IndexError):
                    next_num = Certificate.objects.count() + 1
            self.certificate_no = f"TR-{year}-{next_num:05d}"
        super().save(*args, **kwargs)
