from django.db import migrations


def seed_content(apps, schema_editor):
    Level = apps.get_model('courses', 'Level')
    Lesson = apps.get_model('courses', 'Lesson')
    VocabularyWord = apps.get_model('courses', 'VocabularyWord')
    Question = apps.get_model('courses', 'Question')

    # ---- Daraja 1: Boshlang'ich (A1) ----
    a1 = Level.objects.create(name="Boshlang'ich", code="A1", order=1,
                               description="Salomlashish, tanishuv va asosiy iboralar")

    l1 = Lesson.objects.create(
        level=a1, order=1, title="Salomlashish",
        content=(
            "Turk tilida salomlashish juda muhim va odob-axloq bilan bog'liq. "
            "Eng ko'p ishlatiladigan salomlashish so'zi — 'Merhaba' (Salom). "
            "Kunning turli vaqtlarida boshqa iboralar ham ishlatiladi: ertalab "
            "'Günaydın' (Xayrli tong), kechqurun 'İyi akşamlar' (Xayrli kech). "
            "Xayrlashganda esa 'Hoşça kal' yoki 'Görüşürüz' (Ko'rishguncha) deyiladi."
        ),
    )
    VocabularyWord.objects.bulk_create([
        VocabularyWord(lesson=l1, order=1, turkish="Merhaba", uzbek="Salom"),
        VocabularyWord(lesson=l1, order=2, turkish="Günaydın", uzbek="Xayrli tong"),
        VocabularyWord(lesson=l1, order=3, turkish="İyi akşamlar", uzbek="Xayrli kech"),
        VocabularyWord(lesson=l1, order=4, turkish="Hoşça kal", uzbek="Xayr (qoluvchiga)"),
        VocabularyWord(lesson=l1, order=5, turkish="Görüşürüz", uzbek="Ko'rishguncha"),
        VocabularyWord(lesson=l1, order=6, turkish="Nasılsın?", uzbek="Qalaysiz?"),
        VocabularyWord(lesson=l1, order=7, turkish="İyiyim, teşekkürler", uzbek="Yaxshiman, rahmat"),
    ])
    Question.objects.bulk_create([
        Question(lesson=l1, text="'Salom' turkchada qanday aytiladi?",
                 option_a="Merhaba", option_b="Hoşça kal", option_c="Günaydın", option_d="Nasılsın",
                 correct_option='a'),
        Question(lesson=l1, text="'Xayrli tong' turkchada qanday bo'ladi?",
                 option_a="İyi akşamlar", option_b="Günaydın", option_c="Görüşürüz", option_d="Merhaba",
                 correct_option='b'),
        Question(lesson=l1, text="'Nasılsın?' savolining ma'nosi nima?",
                 option_a="Ismingiz nima?", option_b="Qayerdansiz?", option_c="Qalaysiz?", option_d="Necha yoshdasiz?",
                 correct_option='c'),
    ])

    l2 = Lesson.objects.create(
        level=a1, order=2, title="Tanishuv",
        content=(
            "O'zingizni tanishtirish uchun 'Benim adım ...' (Mening ismim ...) iborasidan "
            "foydalaniladi. Kimningdir ismini so'rash uchun 'Adın ne?' (Isming nima?) deyiladi. "
            "Qayerdan ekanligingizni aytish uchun 'Ben Özbekistan'danım' (Men O'zbekistondanman) "
            "kabi jumla tuziladi."
        ),
    )
    VocabularyWord.objects.bulk_create([
        VocabularyWord(lesson=l2, order=1, turkish="Benim adım...", uzbek="Mening ismim..."),
        VocabularyWord(lesson=l2, order=2, turkish="Adın ne?", uzbek="Isming nima?"),
        VocabularyWord(lesson=l2, order=3, turkish="Memnun oldum", uzbek="Tanishganimdan xursandman"),
        VocabularyWord(lesson=l2, order=4, turkish="Nerelisin?", uzbek="Qayerliksiz?"),
        VocabularyWord(lesson=l2, order=5, turkish="Özbekistan'danım", uzbek="O'zbekistondanman"),
    ])
    Question.objects.bulk_create([
        Question(lesson=l2, text="'Isming nima?' turkchada qanday bo'ladi?",
                 option_a="Adın ne?", option_b="Nerelisin?", option_c="Nasılsın?", option_d="Memnun oldum",
                 correct_option='a'),
        Question(lesson=l2, text="'Tanishganimdan xursandman' iborasi qaysi?",
                 option_a="Benim adım", option_b="Memnun oldum", option_c="Hoşça kal", option_d="Adın ne",
                 correct_option='b'),
    ])

    # ---- Daraja 2: O'rta (A2) ----
    a2 = Level.objects.create(name="O'rta", code="A2", order=2,
                               description="Sonlar, kundalik iboralar va oddiy suhbat")

    l3 = Lesson.objects.create(
        level=a2, order=1, title="Sonlar",
        content=(
            "Turk tilida sonlarni bilish savdo, telefon raqami yoki narx aytishda juda kerak bo'ladi. "
            "1 dan 10 gacha: bir, iki, üç, dört, beş, altı, yedi, sekiz, dokuz, on."
        ),
    )
    VocabularyWord.objects.bulk_create([
        VocabularyWord(lesson=l3, order=1, turkish="Bir", uzbek="Bir (1)"),
        VocabularyWord(lesson=l3, order=2, turkish="İki", uzbek="Ikki (2)"),
        VocabularyWord(lesson=l3, order=3, turkish="Üç", uzbek="Uch (3)"),
        VocabularyWord(lesson=l3, order=4, turkish="Dört", uzbek="To'rt (4)"),
        VocabularyWord(lesson=l3, order=5, turkish="Beş", uzbek="Besh (5)"),
        VocabularyWord(lesson=l3, order=6, turkish="On", uzbek="O'n (10)"),
    ])
    Question.objects.bulk_create([
        Question(lesson=l3, text="Turkchada '5' soni qanday aytiladi?",
                 option_a="Dört", option_b="Beş", option_c="Altı", option_d="On",
                 correct_option='b'),
        Question(lesson=l3, text="'On' soni nechaga teng?",
                 option_a="1", option_b="5", option_c="10", option_d="100",
                 correct_option='c'),
    ])

    l4 = Lesson.objects.create(
        level=a2, order=2, title="Kundalik iboralar",
        content=(
            "Kundalik hayotda tez-tez ishlatiladigan iboralar: 'Teşekkür ederim' (Rahmat), "
            "'Rica ederim' (Marhamat/Arzimaydi), 'Lütfen' (Iltimos), 'Özür dilerim' (Kechirasiz), "
            "'Evet' (Ha), 'Hayır' (Yo'q)."
        ),
    )
    VocabularyWord.objects.bulk_create([
        VocabularyWord(lesson=l4, order=1, turkish="Teşekkür ederim", uzbek="Rahmat"),
        VocabularyWord(lesson=l4, order=2, turkish="Rica ederim", uzbek="Marhamat"),
        VocabularyWord(lesson=l4, order=3, turkish="Lütfen", uzbek="Iltimos"),
        VocabularyWord(lesson=l4, order=4, turkish="Özür dilerim", uzbek="Kechirasiz"),
        VocabularyWord(lesson=l4, order=5, turkish="Evet", uzbek="Ha"),
        VocabularyWord(lesson=l4, order=6, turkish="Hayır", uzbek="Yo'q"),
    ])
    Question.objects.bulk_create([
        Question(lesson=l4, text="'Rahmat' so'zi turkchada qanday bo'ladi?",
                 option_a="Lütfen", option_b="Teşekkür ederim", option_c="Hayır", option_d="Evet",
                 correct_option='b'),
        Question(lesson=l4, text="'Yo'q' so'zining turkchasi qaysi?",
                 option_a="Evet", option_b="Hayır", option_c="Lütfen", option_d="Rica ederim",
                 correct_option='b'),
    ])

    # ---- Yakuniy imtihon savollari havzasi (lesson=None) ----
    Question.objects.bulk_create([
        Question(lesson=None, text="'Salom' so'zining turkchasi?",
                 option_a="Merhaba", option_b="Hayır", option_c="Beş", option_d="Lütfen", correct_option='a'),
        Question(lesson=None, text="'Rahmat' so'zining turkchasi?",
                 option_a="Özür dilerim", option_b="Teşekkür ederim", option_c="Adın ne", option_d="On",
                 correct_option='b'),
        Question(lesson=None, text="'Mening ismim...' iborasi qanday boshlanadi?",
                 option_a="Benim adım", option_b="Nerelisin", option_c="Görüşürüz", option_d="Evet",
                 correct_option='a'),
        Question(lesson=None, text="'10' soni turkchada?",
                 option_a="Bir", option_b="Beş", option_c="On", option_d="Üç", correct_option='c'),
        Question(lesson=None, text="'Ha' so'zining turkchasi?",
                 option_a="Hayır", option_b="Evet", option_c="Lütfen", option_d="Özür dilerim",
                 correct_option='b'),
        Question(lesson=None, text="'Iltimos' so'zining turkchasi?",
                 option_a="Lütfen", option_b="Rica ederim", option_c="Nasılsın", option_d="Dört",
                 correct_option='a'),
        Question(lesson=None, text="'Xayrli tong' iborasi qanday bo'ladi?",
                 option_a="İyi akşamlar", option_b="Günaydın", option_c="Hoşça kal", option_d="Merhaba",
                 correct_option='b'),
        Question(lesson=None, text="'Qalaysiz?' savoli turkchada?",
                 option_a="Adın ne?", option_b="Nerelisin?", option_c="Nasılsın?", option_d="Kaç yaşındasın?",
                 correct_option='c'),
    ])


def remove_content(apps, schema_editor):
    Level = apps.get_model('courses', 'Level')
    Level.objects.filter(code__in=['A1', 'A2']).delete()
    Question = apps.get_model('courses', 'Question')
    Question.objects.filter(lesson__isnull=True).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_content, remove_content),
    ]
