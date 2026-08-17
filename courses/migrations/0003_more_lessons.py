from django.db import migrations


def seed_more_content(apps, schema_editor):
    Level = apps.get_model('courses', 'Level')
    Lesson = apps.get_model('courses', 'Lesson')
    VocabularyWord = apps.get_model('courses', 'VocabularyWord')
    Question = apps.get_model('courses', 'Question')

    a1 = Level.objects.get(code='A1')
    a2 = Level.objects.get(code='A2')

    # ---- A1 ga qo'shimcha darslar ----
    l5 = Lesson.objects.create(
        level=a1, order=3, title="Oila a'zolari",
        content=(
            "Oila a'zolarini turk tilida bilish kundalik suhbatlar uchun juda muhim. "
            "Ota-ona 'anne' (ona) va 'baba' (ota) deb ataladi. Aka-uka va opa-singil "
            "uchun umumiy so'z 'kardeş', lekin katta aka — 'ağabey', katta opa — 'abla' "
            "deb alohida ham aytiladi."
        ),
    )
    VocabularyWord.objects.bulk_create([
        VocabularyWord(lesson=l5, order=1, turkish="Aile", uzbek="Oila"),
        VocabularyWord(lesson=l5, order=2, turkish="Anne", uzbek="Ona"),
        VocabularyWord(lesson=l5, order=3, turkish="Baba", uzbek="Ota"),
        VocabularyWord(lesson=l5, order=4, turkish="Kardeş", uzbek="Aka-uka/opa-singil"),
        VocabularyWord(lesson=l5, order=5, turkish="Abla", uzbek="Katta opa"),
        VocabularyWord(lesson=l5, order=6, turkish="Ağabey", uzbek="Katta aka"),
        VocabularyWord(lesson=l5, order=7, turkish="Çocuk", uzbek="Bola"),
    ])
    Question.objects.bulk_create([
        Question(lesson=l5, text="'Ona' so'zi turkchada qanday bo'ladi?",
                 option_a="Baba", option_b="Anne", option_c="Abla", option_d="Aile", correct_option='b'),
        Question(lesson=l5, text="'Oila' so'zining turkchasi?",
                 option_a="Aile", option_b="Çocuk", option_c="Kardeş", option_d="Ağabey", correct_option='a'),
        Question(lesson=l5, text="'Katta opa' turkchada nima deyiladi?",
                 option_a="Ağabey", option_b="Anne", option_c="Abla", option_d="Baba", correct_option='c'),
    ])

    l6 = Lesson.objects.create(
        level=a1, order=4, title="Ranglar",
        content=(
            "Ranglarni bilish kiyim-kechak yoki narsalarni tasvirlashda kerak bo'ladi. "
            "Eng asosiy ranglar: kırmızı (qizil), mavi (ko'k), yeşil (yashil), sarı (sariq), "
            "siyah (qora), beyaz (oq)."
        ),
    )
    VocabularyWord.objects.bulk_create([
        VocabularyWord(lesson=l6, order=1, turkish="Kırmızı", uzbek="Qizil"),
        VocabularyWord(lesson=l6, order=2, turkish="Mavi", uzbek="Ko'k"),
        VocabularyWord(lesson=l6, order=3, turkish="Yeşil", uzbek="Yashil"),
        VocabularyWord(lesson=l6, order=4, turkish="Sarı", uzbek="Sariq"),
        VocabularyWord(lesson=l6, order=5, turkish="Siyah", uzbek="Qora"),
        VocabularyWord(lesson=l6, order=6, turkish="Beyaz", uzbek="Oq"),
    ])
    Question.objects.bulk_create([
        Question(lesson=l6, text="'Ko'k' rangi turkchada qanday bo'ladi?",
                 option_a="Yeşil", option_b="Mavi", option_c="Sarı", option_d="Siyah", correct_option='b'),
        Question(lesson=l6, text="'Qora' rangining turkchasi?",
                 option_a="Beyaz", option_b="Kırmızı", option_c="Siyah", option_d="Yeşil", correct_option='c'),
    ])

    # ---- A2 ga qo'shimcha darslar ----
    l7 = Lesson.objects.create(
        level=a2, order=3, title="Ovqatlar",
        content=(
            "Restoranda yoki bozorda kerak bo'ladigan asosiy ovqat nomlari: 'ekmek' (non), "
            "'su' (suv), 'çay' (choy), 'kahve' (qahva), 'et' (go'sht), 'meyve' (meva), "
            "'sebze' (sabzavot)."
        ),
    )
    VocabularyWord.objects.bulk_create([
        VocabularyWord(lesson=l7, order=1, turkish="Ekmek", uzbek="Non"),
        VocabularyWord(lesson=l7, order=2, turkish="Su", uzbek="Suv"),
        VocabularyWord(lesson=l7, order=3, turkish="Çay", uzbek="Choy"),
        VocabularyWord(lesson=l7, order=4, turkish="Kahve", uzbek="Qahva"),
        VocabularyWord(lesson=l7, order=5, turkish="Et", uzbek="Go'sht"),
        VocabularyWord(lesson=l7, order=6, turkish="Meyve", uzbek="Meva"),
        VocabularyWord(lesson=l7, order=7, turkish="Sebze", uzbek="Sabzavot"),
    ])
    Question.objects.bulk_create([
        Question(lesson=l7, text="'Non' so'zining turkchasi?",
                 option_a="Su", option_b="Ekmek", option_c="Çay", option_d="Et", correct_option='b'),
        Question(lesson=l7, text="'Choy' turkchada qanday aytiladi?",
                 option_a="Kahve", option_b="Meyve", option_c="Çay", option_d="Sebze", correct_option='c'),
        Question(lesson=l7, text="'Suv' so'zining turkchasi?",
                 option_a="Su", option_b="Et", option_c="Ekmek", option_d="Sebze", correct_option='a'),
    ])

    l8 = Lesson.objects.create(
        level=a2, order=4, title="Vaqt va kalendar",
        content=(
            "Vaqtni ifodalash uchun: 'bugün' (bugun), 'yarın' (ertaga), 'dün' (kecha), "
            "'saat' (soat), 'hafta' (hafta), 'ay' (oy), 'yıl' (yil) so'zlari ishlatiladi."
        ),
    )
    VocabularyWord.objects.bulk_create([
        VocabularyWord(lesson=l8, order=1, turkish="Bugün", uzbek="Bugun"),
        VocabularyWord(lesson=l8, order=2, turkish="Yarın", uzbek="Ertaga"),
        VocabularyWord(lesson=l8, order=3, turkish="Dün", uzbek="Kecha"),
        VocabularyWord(lesson=l8, order=4, turkish="Saat", uzbek="Soat"),
        VocabularyWord(lesson=l8, order=5, turkish="Hafta", uzbek="Hafta"),
        VocabularyWord(lesson=l8, order=6, turkish="Ay", uzbek="Oy"),
        VocabularyWord(lesson=l8, order=7, turkish="Yıl", uzbek="Yil"),
    ])
    Question.objects.bulk_create([
        Question(lesson=l8, text="'Ertaga' so'zining turkchasi?",
                 option_a="Dün", option_b="Yarın", option_c="Bugün", option_d="Hafta", correct_option='b'),
        Question(lesson=l8, text="'Kecha' turkchada qanday bo'ladi?",
                 option_a="Dün", option_b="Yıl", option_c="Ay", option_d="Saat", correct_option='a'),
    ])

    # ---- Yangi daraja: Yuqori (B1) ----
    b1 = Level.objects.create(name="Yuqori", code="B1", order=3,
                               description="Sayohat, ish va murakkabroq suhbat iboralari")

    l9 = Lesson.objects.create(
        level=b1, order=1, title="Sayohat iboralari",
        content=(
            "Sayohat paytida kerak bo'ladigan so'zlar: 'havaalanı' (aeroport), 'otel' "
            "(mehmonxona), 'bilet' (chipta), 'yol' (yo'l), 'şehir' (shahar). "
            "'Nereye gidiyorsunuz?' — 'Qayerga ketyapsiz?' degani."
        ),
    )
    VocabularyWord.objects.bulk_create([
        VocabularyWord(lesson=l9, order=1, turkish="Havaalanı", uzbek="Aeroport"),
        VocabularyWord(lesson=l9, order=2, turkish="Otel", uzbek="Mehmonxona"),
        VocabularyWord(lesson=l9, order=3, turkish="Bilet", uzbek="Chipta"),
        VocabularyWord(lesson=l9, order=4, turkish="Yol", uzbek="Yo'l"),
        VocabularyWord(lesson=l9, order=5, turkish="Şehir", uzbek="Shahar"),
        VocabularyWord(lesson=l9, order=6, turkish="Nereye gidiyorsunuz?", uzbek="Qayerga ketyapsiz?"),
    ])
    Question.objects.bulk_create([
        Question(lesson=l9, text="'Mehmonxona' so'zining turkchasi?",
                 option_a="Otel", option_b="Bilet", option_c="Yol", option_d="Şehir", correct_option='a'),
        Question(lesson=l9, text="'Aeroport' turkchada qanday bo'ladi?",
                 option_a="Şehir", option_b="Havaalanı", option_c="Otel", option_d="Yol", correct_option='b'),
    ])

    l10 = Lesson.objects.create(
        level=b1, order=2, title="Ish va kasblar",
        content=(
            "Kasb nomlari: 'doktor' (shifokor), 'öğretmen' (o'qituvchi), 'mühendis' "
            "(muhandis), 'öğrenci' (talaba). 'Ne iş yapıyorsunuz?' — 'Nima ish qilasiz?' "
            "degan savol."
        ),
    )
    VocabularyWord.objects.bulk_create([
        VocabularyWord(lesson=l10, order=1, turkish="İş", uzbek="Ish"),
        VocabularyWord(lesson=l10, order=2, turkish="Doktor", uzbek="Shifokor"),
        VocabularyWord(lesson=l10, order=3, turkish="Öğretmen", uzbek="O'qituvchi"),
        VocabularyWord(lesson=l10, order=4, turkish="Mühendis", uzbek="Muhandis"),
        VocabularyWord(lesson=l10, order=5, turkish="Öğrenci", uzbek="Talaba"),
    ])
    Question.objects.bulk_create([
        Question(lesson=l10, text="'O'qituvchi' so'zining turkchasi?",
                 option_a="Doktor", option_b="Öğretmen", option_c="Mühendis", option_d="Öğrenci", correct_option='b'),
        Question(lesson=l10, text="'Talaba' turkchada qanday bo'ladi?",
                 option_a="Öğrenci", option_b="İş", option_c="Doktor", option_d="Mühendis", correct_option='a'),
    ])

    # ---- Yakuniy imtihon havzasiga qo'shimcha savollar ----
    Question.objects.bulk_create([
        Question(lesson=None, text="'Oila' so'zining turkchasi?",
                 option_a="Aile", option_b="Kardeş", option_c="Anne", option_d="Baba", correct_option='a'),
        Question(lesson=None, text="'Qizil' rangi turkchada?",
                 option_a="Mavi", option_b="Kırmızı", option_c="Yeşil", option_d="Beyaz", correct_option='b'),
        Question(lesson=None, text="'Non' so'zining turkchasi?",
                 option_a="Ekmek", option_b="Su", option_c="Çay", option_d="Et", correct_option='a'),
        Question(lesson=None, text="'Bugun' turkchada qanday bo'ladi?",
                 option_a="Yarın", option_b="Dün", option_c="Bugün", option_d="Hafta", correct_option='c'),
        Question(lesson=None, text="'Mehmonxona' so'zining turkchasi?",
                 option_a="Otel", option_b="Şehir", option_c="Bilet", option_d="Yol", correct_option='a'),
        Question(lesson=None, text="'Shifokor' so'zining turkchasi?",
                 option_a="Öğretmen", option_b="Doktor", option_c="Öğrenci", option_d="Mühendis", correct_option='b'),
        Question(lesson=None, text="'Katta aka' turkchada qanday bo'ladi?",
                 option_a="Abla", option_b="Ağabey", option_c="Kardeş", option_d="Baba", correct_option='b'),
        Question(lesson=None, text="'Sabzavot' so'zining turkchasi?",
                 option_a="Meyve", option_b="Sebze", option_c="Et", option_d="Ekmek", correct_option='b'),
        Question(lesson=None, text="'Yashil' rangi turkchada?",
                 option_a="Sarı", option_b="Siyah", option_c="Yeşil", option_d="Beyaz", correct_option='c'),
        Question(lesson=None, text="'Yil' so'zining turkchasi?",
                 option_a="Ay", option_b="Hafta", option_c="Saat", option_d="Yıl", correct_option='d'),
    ])


def remove_more_content(apps, schema_editor):
    Level = apps.get_model('courses', 'Level')
    Level.objects.filter(code='B1').delete()
    Lesson = apps.get_model('courses', 'Lesson')
    Lesson.objects.filter(title__in=[
        "Oila a'zolari", "Ranglar", "Ovqatlar", "Vaqt va kalendar",
    ]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_seed_content'),
    ]

    operations = [
        migrations.RunPython(seed_more_content, remove_more_content),
    ]
