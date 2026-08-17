import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nomi')),
                ('code', models.CharField(blank=True, max_length=10, verbose_name='Kod (masalan A1)')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Qisqa tavsif')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Tartib raqami')),
                ('is_active', models.BooleanField(default=True, verbose_name='Faol')),
            ],
            options={
                'verbose_name': 'Daraja',
                'verbose_name_plural': 'Darajalar',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Sarlavha')),
                ('content', models.TextField(verbose_name='Dars matni (tushuntirish)')),
                ('video_url', models.URLField(blank=True, verbose_name='Video havolasi (ixtiyoriy)')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Tartib raqami')),
                ('is_active', models.BooleanField(default=True, verbose_name='Faol')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqt")),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='darslar', to='courses.level', verbose_name='Daraja')),
            ],
            options={
                'verbose_name': 'Dars',
                'verbose_name_plural': 'Darslar',
                'ordering': ['level__order', 'order'],
            },
        ),
        migrations.CreateModel(
            name='VocabularyWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turkish', models.CharField(max_length=150, verbose_name="Turkcha so'z/ibora")),
                ('uzbek', models.CharField(max_length=150, verbose_name="O'zbekcha ma'nosi")),
                ('example', models.CharField(blank=True, max_length=255, verbose_name='Misol gap (ixtiyoriy)')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Tartib')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lugat', to='courses.lesson', verbose_name='Dars')),
            ],
            options={
                'verbose_name': "Lug'at so'zi",
                'verbose_name_plural': "Lug'at so'zlari",
                'ordering': ['order', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=400, verbose_name='Savol matni')),
                ('option_a', models.CharField(max_length=200, verbose_name='A varianti')),
                ('option_b', models.CharField(max_length=200, verbose_name='B varianti')),
                ('option_c', models.CharField(max_length=200, verbose_name='C varianti')),
                ('option_d', models.CharField(max_length=200, verbose_name='D varianti')),
                ('correct_option', models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')], max_length=1, verbose_name="To'g'ri javob")),
                ('explanation', models.CharField(blank=True, max_length=300, verbose_name='Tushuntirish (ixtiyoriy)')),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='savollar', to='courses.lesson', verbose_name="Dars (bo'sh bo'lsa — yakuniy imtihon savoli)")),
            ],
            options={
                'verbose_name': 'Test savoli',
                'verbose_name_plural': 'Test savollari',
            },
        ),
        migrations.CreateModel(
            name='LessonCompletion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('best_score_percent', models.PositiveIntegerField(default=0, verbose_name="Eng yaxshi natija (%)")),
                ('attempts', models.PositiveIntegerField(default=0, verbose_name='Urinishlar soni')),
                ('completed_at', models.DateTimeField(auto_now=True, verbose_name='Tugatilgan vaqt')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tugatganlar', to='courses.lesson', verbose_name='Dars')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tugatilgan_darslar', to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi')),
            ],
            options={
                'verbose_name': 'Dars natijasi',
                'verbose_name_plural': 'Dars natijalari',
            },
        ),
        migrations.CreateModel(
            name='ExamAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveIntegerField(verbose_name="To'g'ri javoblar soni")),
                ('total', models.PositiveIntegerField(verbose_name='Jami savollar soni')),
                ('percent', models.PositiveIntegerField(verbose_name='Foiz natija')),
                ('passed', models.BooleanField(default=False, verbose_name="O'tdi")),
                ('taken_at', models.DateTimeField(auto_now_add=True, verbose_name='Topshirilgan vaqt')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imtihon_urinishlari', to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi')),
            ],
            options={
                'verbose_name': 'Imtihon urinishi',
                'verbose_name_plural': 'Imtihon urinishlari',
                'ordering': ['-taken_at'],
            },
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_no', models.CharField(blank=True, max_length=30, unique=True, verbose_name='Sertifikat raqami')),
                ('issued_at', models.DateTimeField(auto_now_add=True, verbose_name='Berilgan sana')),
                ('exam_attempt', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sertifikat', to='courses.examattempt', verbose_name='Imtihon urinishi')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sertifikatlar', to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi')),
            ],
            options={
                'verbose_name': 'Sertifikat',
                'verbose_name_plural': 'Sertifikatlar',
                'ordering': ['-issued_at'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='lessoncompletion',
            unique_together={('user', 'lesson')},
        ),
    ]
