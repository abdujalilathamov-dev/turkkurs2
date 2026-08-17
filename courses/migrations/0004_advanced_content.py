from django.db import migrations, models


def seed_advanced_content(apps, schema_editor):
    Level = apps.get_model('courses', 'Level')
    Lesson = apps.get_model('courses', 'Lesson')
    VocabularyWord = apps.get_model('courses', 'VocabularyWord')
    Question = apps.get_model('courses', 'Question')

    a1 = Level.objects.get(code='A1')
    a2 = Level.objects.get(code='A2')
    b1 = Level.objects.get(code='B1')

    # ==================================================================
    # A1 — Alifbo va talaffuz (mavjud darslardan OLDIN joylashadi)
    # ==================================================================
    Lesson.objects.filter(level=a1, order__gte=1).update(order=models.F('order') + 2)

    alifbo = Lesson.objects.create(
        level=a1, order=1, title="Turk alifbosi",
        content=(
            "Turk alifbosida 29 ta harf bor. U lotin alifbosiga asoslangan, lekin "
            "inglizchadagi Q, W, X harflari yo'q. O'zbek tilida ham lotin alifbosi "
            "ishlatilgani uchun, ko'p harflar sizga tanish bo'ladi.\n\n"
            "MAXSUS HARFLAR (o'zbekchada aniq muqobili bo'lmagan yoki boshqacha o'qiladigan):\n\n"
            "Ç ç — 'ch' tovushi beradi (o'zbekcha 'ch' kabi). Misol: çay — choy\n"
            "Ğ ğ — deyarli talaffuz qilinmaydi, o'zidan oldingi unlini cho'zadi. Misol: dağ — tog'\n"
            "I ı (nuqtasiz) — 'ы' ga o'xshash, og'iz keng ochilmagan holda aytiladi. Misol: ışık — yorug'lik\n"
            "İ i (nuqtali) — oddiy 'i' tovushi. Misol: iyi — yaxshi\n"
            "Ö ö — o'zbekcha 'o'' harfiga o'xshaydi, lablar yumaloqlanadi. Misol: ödev — uy vazifasi\n"
            "Ş ş — 'sh' tovushi (o'zbekcha 'sh' kabi). Misol: şeker — shakar\n"
            "Ü ü — 'yumshoq u', lablar yumaloqlanib aytiladi. Misol: ütü — dazmol\n\n"
            "DIQQAT: 'C' harfi turk tilida 'j' kabi o'qiladi (masalan 'cami' — 'jami' "
            "deb o'qiladi), inglizcha 'c' kabi emas! Qolgan harflar (a, b, d, e, f, g, "
            "h, j, k, l, m, n, o, p, r, s, t, u, v, y, z) o'zbek-lotin alifbosidagi "
            "harflarga juda yaqin talaffuz qilinadi."
        ),
    )
    VocabularyWord.objects.bulk_create([
        VocabularyWord(lesson=alifbo, order=1, turkish="Çay", uzbek="Choy", example="Çay içer misin? — Choy ichasanmi?"),
        VocabularyWord(lesson=alifbo, order=2, turkish="Dağ", uzbek="Tog'"),
        VocabularyWord(lesson=alifbo, order=3, turkish="Işık", uzbek="Yorug'lik"),
        VocabularyWord(lesson=alifbo, order=4, turkish="İyi", uzbek="Yaxshi"),
        VocabularyWord(lesson=alifbo, order=5, turkish="Ödev", uzbek="Uy vazifasi"),
        VocabularyWord(lesson=alifbo, order=6, turkish="Şeker", uzbek="Shakar"),
        VocabularyWord(lesson=alifbo, order=7, turkish="Ütü", uzbek="Dazmol"),
        VocabularyWord(lesson=alifbo, order=8, turkish="Cami", uzbek="Machit ('j' deb o'qiladi)"),
    ])
    Question.objects.bulk_create([
        Question(lesson=alifbo, text="Turk alifbosida nechta harf bor?",
                 option_a="26", option_b="29", option_c="30", option_d="33", correct_option='b'),
        Question(lesson=alifbo, text="Turk alifbosida qaysi harflar yo'q?",
                 option_a="Q, W, X", option_b="F, J, L", option_c="C, Ç, Ş", option_d="Ö, Ü, I",
                 correct_option='a'),
        Question(lesson=alifbo, text="'Ç' harfi qanday tovush beradi?",
                 option_a="'j'", option_b="'sh'", option_c="'ch'", option_d="'s'", correct_option='c'),
        Question(lesson=alifbo, text="Turk tilida 'C' harfi qanday o'qiladi?",
                 option_a="'s' kabi", option_b="'j' kabi", option_c="'k' kabi", option_d="'ch' kabi",
                 correct_option='b'),
        Question(lesson=alifbo, text="'Ğ' harfi haqida qaysi fikr to'g'ri?",
                 option_a="'g' kabi qattiq aytiladi", option_b="Deyarli talaffuz qilinmaydi, unlini cho'zadi",
                 option_c="'k' kabi aytiladi", option_d="Umuman ishlatilmaydi", correct_option='b'),
    ])

    talaffuz = Lesson.objects.create(
        level=a1, order=2, title="Talaffuz qoidalari",
        content=(
            "Turk tilini to'g'ri o'qish uchun eng muhim qoida — UNLILAR UYG'UNLIGI "
            "(ünlü uyumu). Bu qoidaga ko'ra, so'zga qo'shimcha qo'shilganda, "
            "qo'shimchadagi unli tovush so'z tugaydigan unliga 'mos' bo'lishi kerak.\n\n"
            "Sodda misolda ko'plik qo'shimchasi -lar / -ler orqali tushuntiramiz:\n"
            "— Agar so'zning oxirgi unlisi 'yo'g'on' (a, ı, o, u) bo'lsa — qo'shimcha -lar bo'ladi.\n"
            "  Misol: kitap (kitob) → kitaplar (kitoblar)\n"
            "— Agar so'zning oxirgi unlisi 'ingichka' (e, i, ö, ü) bo'lsa — qo'shimcha -ler bo'ladi.\n"
            "  Misol: ev (uy) → evler (uylar)\n\n"
            "Bu qoida deyarli barcha qo'shimchalarga (kelishik, egalik, fe'l "
            "qo'shimchalari) taalluqli, shuning uchun uni yaxshi tushunib olish "
            "juda muhim.\n\n"
            "URG'U: Turk tilida urg'u odatda so'zning OXIRGI bo'g'inida bo'ladi "
            "(o'zbek tilidagiga o'xshab). Masalan: kitap → ki-TAP, öğretmen → öğret-MEN. "
            "Ba'zi joy nomlari va kirish so'zlarida bu qoidadan istisnolar uchraydi."
        ),
    )
    VocabularyWord.objects.bulk_create([
        VocabularyWord(lesson=talaffuz, order=1, turkish="Kitap → Kitaplar", uzbek="Kitob → Kitoblar (yo'g'on unli)"),
        VocabularyWord(lesson=talaffuz, order=2, turkish="Ev → Evler", uzbek="Uy → Uylar (ingichka unli)"),
        VocabularyWord(lesson=talaffuz, order=3, turkish="Göz → Gözler", uzbek="Ko'z → Ko'zlar (ingichka unli)"),
        VocabularyWord(lesson=talaffuz, order=4, turkish="Yol → Yollar", uzbek="Yo'l → Yo'llar (yo'g'on unli)"),
    ])
    Question.objects.bulk_create([
        Question(lesson=talaffuz, text="'Kitap' so'ziga ko'plik qo'shimchasi qanday qo'shiladi?",
                 option_a="-ler", option_b="-lar", option_c="-lor", option_d="-lir", correct_option='b'),
        Question(lesson=talaffuz, text="'Ev' so'ziga ko'plik qo'shimchasi qanday qo'shiladi?",
                 option_a="-lar", option_b="-lor", option_c="-ler", option_d="-lur", correct_option='c'),
        Question(lesson=talaffuz, text="Turk tilida so'zlarda urg'u odatda qayerga tushadi?",
                 option_a="Birinchi bo'g'inga", option_b="Oxirgi bo'g'inga",
                 option_c="Har doim ikkinchi bo'g'inga", option_d="Urg'u umuman bo'lmaydi",
                 correct_option='b'),
        Question(lesson=talaffuz, text="Bu qoidaning nomi nima?",
                 option_a="Undoshlar yumshashi", option_b="Unlilar uyg'unligi",
                 option_c="Urg'u siljishi", option_d="Bo'g'in qisqarishi", correct_option='b'),
    ])

    # ==================================================================
    # A2 — Reading: Oddiy matn
    # ==================================================================
    reading_a2 = Lesson.objects.create(
        level=a2, order=5, title="O'qish: Yangi tanish",
        content=(
            "TURKCHA MATN:\n"
            "\"Merhaba! Benim adım Ahmet. Ben Türkiye'den geliyorum, İstanbul'da "
            "yaşıyorum. Yirmi beş yaşındayım. Öğretmenim ve okulda çocuklara "
            "İngilizce öğretiyorum. Ailem çok kalabalık: annem, babam, iki "
            "kardeşim var. Boş zamanlarımda kitap okumayı ve yüzmeyi severim.\"\n\n"
            "O'ZBEKCHA TARJIMASI:\n"
            "\"Salom! Mening ismim Ahmad. Men Turkiyadanman, Istanbulda "
            "yashayman. Yigirma besh yoshdaman. Men o'qituvchiman va maktabda "
            "bolalarga ingliz tilini o'rgataman. Oilam juda katta: onam, otam, "
            "ikki aka-ukam bor. Bo'sh vaqtimda kitob o'qishni va suzishni yaxshi "
            "ko'raman.\"\n\n"
            "Matnni diqqat bilan qayta o'qing va lug'atdagi yangi so'zlarni "
            "yodlab oling, so'ng pastdagi testni ishlang."
        ),
    )
    VocabularyWord.objects.bulk_create([
        VocabularyWord(lesson=reading_a2, order=1, turkish="Geliyorum", uzbek="Kelyapman/...danman", example="gelmek — kelmoq fe'lidan"),
        VocabularyWord(lesson=reading_a2, order=2, turkish="Yaşıyorum", uzbek="Yashayman", example="yaşamak — yashamoq fe'lidan"),
        VocabularyWord(lesson=reading_a2, order=3, turkish="Öğretiyorum", uzbek="O'rgataman", example="öğretmek — o'rgatmoq fe'lidan"),
        VocabularyWord(lesson=reading_a2, order=4, turkish="Severim", uzbek="Yaxshi ko'raman", example="sevmek — yaxshi ko'rmoq fe'lidan"),
        VocabularyWord(lesson=reading_a2, order=5, turkish="Kalabalık", uzbek="Katta/gavjum (oila, joy haqida)"),
    ])
    Question.objects.bulk_create([
        Question(lesson=reading_a2, text="Ahmet necha yoshda?",
                 option_a="20", option_b="25", option_c="30", option_d="35", correct_option='b'),
        Question(lesson=reading_a2, text="Ahmet qaysi shaharda yashaydi?",
                 option_a="Ankara", option_b="Izmir", option_c="İstanbul", option_d="Bursa",
                 correct_option='c'),
        Question(lesson=reading_a2, text="Ahmetning kasbi nima?",
                 option_a="Shifokor", option_b="O'qituvchi", option_c="Muhandis", option_d="Talaba",
                 correct_option='b'),
        Question(lesson=reading_a2, text="Ahmet bo'sh vaqtida nima qilishni yaxshi ko'radi?",
                 option_a="Futbol o'ynash", option_b="Kitob o'qish va suzish",
                 option_c="Ovqat pishirish", option_d="Rasm chizish", correct_option='b'),
        Question(lesson=reading_a2, text="Ahmetning oilasida yana kimlar bor?",
                 option_a="Faqat onasi", option_b="Onasi, otasi va ikki aka-ukasi",
                 option_c="Faqat otasi", option_d="Xotini va bolalari", correct_option='b'),
    ])

    # ==================================================================
    # B1 — qo'shimcha darslar: grammatika va o'qish
    # ==================================================================
    grammar_b1 = Lesson.objects.create(
        level=b1, order=3, title="O'tgan zamon (-di)",
        content=(
            "Turk tilida o'tgan zamon fe'lga -di / -dı / -du / -dü (yoki qattiq "
            "undoshdan keyin -ti / -tı / -tu / -tü) qo'shimchasi qo'shish orqali "
            "yasaladi. Qaysi variant tanlanishi unlilar uyg'unligi qoidasiga bog'liq.\n\n"
            "'Gelmek' (kelmoq) fe'lining o'tgan zamondagi tuslanishi:\n"
            "Geldim — Keldim\n"
            "Geldin — Kelding\n"
            "Geldi — Keldi\n"
            "Geldik — Keldik\n"
            "Geldiniz — Keldingiz\n"
            "Geldiler — Kelishdi\n\n"
            "Boshqa fe'llar bilan misollar: gitmek (bormoq) → gittim (bordim), "
            "yapmak (qilmoq) → yaptım (qildim), görmek (ko'rmoq) → gördüm (ko'rdim)."
        ),
    )
    VocabularyWord.objects.bulk_create([
        VocabularyWord(lesson=grammar_b1, order=1, turkish="Geldim", uzbek="Keldim"),
        VocabularyWord(lesson=grammar_b1, order=2, turkish="Gittim", uzbek="Bordim", example="gitmek — bormoq"),
        VocabularyWord(lesson=grammar_b1, order=3, turkish="Yaptım", uzbek="Qildim", example="yapmak — qilmoq"),
        VocabularyWord(lesson=grammar_b1, order=4, turkish="Gördüm", uzbek="Ko'rdim", example="görmek — ko'rmoq"),
    ])
    Question.objects.bulk_create([
        Question(lesson=grammar_b1, text="'Geldim' so'zining ma'nosi nima?",
                 option_a="Kelaman", option_b="Keldim", option_c="Kelasan", option_d="Kelgin",
                 correct_option='b'),
        Question(lesson=grammar_b1, text="'Bormoq' fe'lining turkchasi qaysi?",
                 option_a="Gelmek", option_b="Yapmak", option_c="Gitmek", option_d="Görmek",
                 correct_option='c'),
        Question(lesson=grammar_b1, text="O'tgan zamon qo'shimchasi asosan qaysi tovush bilan boshlanadi?",
                 option_a="-ecek", option_b="-di", option_c="-yor", option_d="-miş", correct_option='b'),
    ])

    reading_b1 = Lesson.objects.create(
        level=b1, order=4, title="O'qish: Sayohat kundaligi",
        content=(
            "TURKCHA MATN:\n"
            "\"Geçen hafta İzmir'e gittim. Otobüsle sekiz saat yol gittik. Şehir "
            "çok güzeldi, deniz kenarında yürüdük. Akşam yerel bir restoranda "
            "balık yedik. Üç gün kaldık ve sonra eve döndük.\"\n\n"
            "O'ZBEKCHA TARJIMASI:\n"
            "\"O'tgan hafta Izmirga bordim. Avtobusda sakkiz soat yo'l yurdik. "
            "Shahar juda chiroyli edi, dengiz bo'yida yurdik. Kechqurun mahalliy "
            "restoranda baliq yedik. Uch kun qoldik va keyin uyga qaytdik.\""
        ),
    )
    VocabularyWord.objects.bulk_create([
        VocabularyWord(lesson=reading_b1, order=1, turkish="Geçen hafta", uzbek="O'tgan hafta"),
        VocabularyWord(lesson=reading_b1, order=2, turkish="Deniz kenarı", uzbek="Dengiz bo'yi"),
        VocabularyWord(lesson=reading_b1, order=3, turkish="Yürüdük", uzbek="Yurdik (piyoda)"),
        VocabularyWord(lesson=reading_b1, order=4, turkish="Döndük", uzbek="Qaytdik"),
    ])
    Question.objects.bulk_create([
        Question(lesson=reading_b1, text="Izmirga necha soat yo'l yurishdi?",
                 option_a="5", option_b="8", option_c="10", option_d="12", correct_option='b'),
        Question(lesson=reading_b1, text="Kechqurun nima yeyishdi?",
                 option_a="Go'sht", option_b="Tovuq", option_c="Baliq", option_d="Sabzavot",
                 correct_option='c'),
        Question(lesson=reading_b1, text="Izmirda necha kun qolishdi?",
                 option_a="2", option_b="3", option_c="5", option_d="7", correct_option='b'),
    ])

    # ==================================================================
    # YANGI DARAJA: B2 — Yuqori-o'rta
    # ==================================================================
    b2 = Level.objects.create(name="Yuqori-o'rta", code="B2", order=4,
                               description="Kelasi zamon, gazeta matnlari va idiomalar")

    kelasi = Lesson.objects.create(
        level=b2, order=1, title="Kelasi zamon (-ecek)",
        content=(
            "Kelasi zamon fe'lga -ecek / -acak qo'shimchasi qo'shish orqali "
            "yasaladi (unlilar uyg'unligiga qarab tanlanadi).\n\n"
            "'Gitmek' (bormoq) fe'lining kelasi zamondagi tuslanishi:\n"
            "Gideceğim — Boraman\n"
            "Gideceksin — Borasan\n"
            "Gidecek — Boradi\n"
            "Gideceğiz — Boramiz\n"
            "Gideceksiniz — Borasiz\n"
            "Gidecekler — Borishadi\n\n"
            "Boshqa misollar: yapmak (qilmoq) → yapacağım (qilaman), "
            "görmek (ko'rmoq) → göreceğiz (ko'ramiz)."
        ),
    )
    VocabularyWord.objects.bulk_create([
        VocabularyWord(lesson=kelasi, order=1, turkish="Gideceğim", uzbek="Boraman"),
        VocabularyWord(lesson=kelasi, order=2, turkish="Göreceğiz", uzbek="Ko'ramiz"),
        VocabularyWord(lesson=kelasi, order=3, turkish="Yapacaksın", uzbek="Qilasan"),
    ])
    Question.objects.bulk_create([
        Question(lesson=kelasi, text="Kelasi zamon qo'shimchasi qaysi?",
                 option_a="-di", option_b="-yor", option_c="-ecek/-acak", option_d="-miş",
                 correct_option='c'),
        Question(lesson=kelasi, text="'Gideceğim' so'zining ma'nosi?",
                 option_a="Bordim", option_b="Boraman", option_c="Boryapman", option_d="Borgin",
                 correct_option='b'),
    ])

    gazeta = Lesson.objects.create(
        level=b2, order=2, title="O'qish: Ob-havo xabari",
        content=(
            "TURKCHA MATN:\n"
            "\"Türkiye'nin farklı bölgelerinde hava durumu bu hafta değişken "
            "olacak. Batı bölgelerinde güneşli ve sıcak hava beklenirken, doğu "
            "bölgelerinde yağmur ve daha serin hava öngörülüyor. Uzmanlar, "
            "önümüzdeki hafta sıcaklıkların yükseleceğini belirtiyor.\"\n\n"
            "O'ZBEKCHA TARJIMASI:\n"
            "\"Turkiyaning turli hududlarida bu hafta ob-havo o'zgaruvchan "
            "bo'ladi. G'arbiy hududlarda quyoshli va issiq havo kutilsa, "
            "sharqiy hududlarda yomg'ir va sovuqroq havo bashorat qilinmoqda. "
            "Mutaxassislar, keyingi hafta harorat ko'tarilishini "
            "ta'kidlamoqda.\""
        ),
    )
    VocabularyWord.objects.bulk_create([
        VocabularyWord(lesson=gazeta, order=1, turkish="Hava durumu", uzbek="Ob-havo"),
        VocabularyWord(lesson=gazeta, order=2, turkish="Değişken", uzbek="O'zgaruvchan"),
        VocabularyWord(lesson=gazeta, order=3, turkish="Uzmanlar", uzbek="Mutaxassislar"),
        VocabularyWord(lesson=gazeta, order=4, turkish="Sıcaklık", uzbek="Harorat"),
    ])
    Question.objects.bulk_create([
        Question(lesson=gazeta, text="G'arbiy hududlarda qanday havo kutilmoqda?",
                 option_a="Yomg'irli va sovuq", option_b="Quyoshli va issiq",
                 option_c="Qorli", option_d="Shamolli", correct_option='b'),
        Question(lesson=gazeta, text="Mutaxassislar keyingi hafta nima bo'lishini aytishmoqda?",
                 option_a="Harorat pasayadi", option_b="Harorat ko'tariladi",
                 option_c="O'zgarish bo'lmaydi", option_d="Qor yog'adi", correct_option='b'),
    ])

    idioma = Lesson.objects.create(
        level=b2, order=3, title="Idiomalar va iboralar",
        content=(
            "Turk tilida kundalik nutqda tez-tez ishlatiladigan idiomalar bor. "
            "Ularni bilish sizga tabiiyroq gapirishga yordam beradi.\n\n"
            "Ağzı açık kalmak — so'zma-so'z 'og'zi ochilib qolmoq' — juda hayron "
            "bo'lish ma'nosida ishlatiladi.\n"
            "Eli açık — so'zma-so'z 'qo'li ochiq' — saxiy odam haqida aytiladi.\n"
            "Kafası karışık — so'zma-so'z 'boshi qorishgan' — fikri chalkash, "
            "band odam haqida.\n"
            "Gözden düşmek — so'zma-so'z 'ko'zdan tushmoq' — obro'sini "
            "yo'qotmoq ma'nosida."
        ),
    )
    VocabularyWord.objects.bulk_create([
        VocabularyWord(lesson=idioma, order=1, turkish="Ağzı açık kalmak", uzbek="Juda hayron bo'lish"),
        VocabularyWord(lesson=idioma, order=2, turkish="Eli açık", uzbek="Saxiy"),
        VocabularyWord(lesson=idioma, order=3, turkish="Kafası karışık", uzbek="Fikri chalkash"),
        VocabularyWord(lesson=idioma, order=4, turkish="Gözden düşmek", uzbek="Obro'sini yo'qotmoq"),
    ])
    Question.objects.bulk_create([
        Question(lesson=idioma, text="'Eli açık' iborasi nimani anglatadi?",
                 option_a="Saxiy odam", option_b="Xasis odam", option_c="Charchagan odam",
                 option_d="Kasal odam", correct_option='a'),
        Question(lesson=idioma, text="'Ağzı açık kalmak' iborasi qanday holatni bildiradi?",
                 option_a="Ochlik", option_b="Juda hayron bo'lish", option_c="Uyqu",
                 option_d="Xursandchilik", correct_option='b'),
    ])

    # ==================================================================
    # YANGI DARAJA: C1 — Yuqori (ilg'or)
    # ==================================================================
    c1 = Level.objects.create(name="Yuqori (ilg'or)", code="C1", order=5,
                               description="Majhul nisbat, ko'chirma gap va adabiy matnlar")

    majhul = Lesson.objects.create(
        level=c1, order=1, title="Majhul nisbat (passiv)",
        content=(
            "Majhul (passiv) nisbat fe'l o'zagiga -il / -in (yoki -l / -n) "
            "qo'shimchasi qo'shish orqali yasaladi. Bu qurilish ish kim "
            "tomonidan bajarilgani muhim bo'lmaganda ishlatiladi.\n\n"
            "Misollar:\n"
            "Yazmak (yozmoq) → Yazılmak (yozilmoq): 'Kitap yazıldı' — Kitob yozildi.\n"
            "Yapmak (qilmoq) → Yapılmak (qilinmoq): 'İş yapıldı' — Ish qilindi.\n"
            "Görmek (ko'rmoq) → Görülmek (ko'rilmoq): 'Film görüldü' — Film ko'rildi."
        ),
    )
    VocabularyWord.objects.bulk_create([
        VocabularyWord(lesson=majhul, order=1, turkish="Yazılmak", uzbek="Yozilmoq"),
        VocabularyWord(lesson=majhul, order=2, turkish="Yapılmak", uzbek="Qilinmoq"),
        VocabularyWord(lesson=majhul, order=3, turkish="Görülmek", uzbek="Ko'rilmoq"),
    ])
    Question.objects.bulk_create([
        Question(lesson=majhul, text="Majhul nisbat qanday yasaladi?",
                 option_a="-ecek qo'shimchasi bilan", option_b="-il/-in qo'shimchasi bilan",
                 option_c="-yor qo'shimchasi bilan", option_d="-miş qo'shimchasi bilan",
                 correct_option='b'),
        Question(lesson=majhul, text="'Yazılmak' so'zining ma'nosi?",
                 option_a="Yozmoq", option_b="O'qimoq", option_c="Yozilmoq", option_d="Chizmoq",
                 correct_option='c'),
    ])

    kochirma = Lesson.objects.create(
        level=c1, order=2, title="Ko'chirma gap (-mış)",
        content=(
            "Turk tilida boshqa birovdan eshitilgan yoki bilvosita ma'lum "
            "bo'lgan ma'lumotni bildirish uchun -mış / -miş / -muş / -müş "
            "qo'shimchasi ishlatiladi (o'zbekchadagi 'ekan' ma'nosiga yaqin).\n\n"
            "Misol: 'Ali gelmiş' — 'Ali kelgan ekan' (buni men o'z ko'zim bilan "
            "ko'rmadim, lekin eshitdim yoki natijasini ko'rdim).\n"
            "Farqi: 'Ali geldi' — 'Ali keldi' (men buni bevosita bilaman/ko'rdim)."
        ),
    )
    VocabularyWord.objects.bulk_create([
        VocabularyWord(lesson=kochirma, order=1, turkish="Gelmiş", uzbek="Kelgan ekan"),
        VocabularyWord(lesson=kochirma, order=2, turkish="Yapmış", uzbek="Qilgan ekan"),
        VocabularyWord(lesson=kochirma, order=3, turkish="Gitmiş", uzbek="Borgan ekan"),
    ])
    Question.objects.bulk_create([
        Question(lesson=kochirma, text="'-mış/-miş' qo'shimchasi nimani bildiradi?",
                 option_a="Kelasi zamonni", option_b="Bevosita ko'rilgan o'tgan zamonni",
                 option_c="Eshitilgan/bilvosita ma'lumotni ('ekan')", option_d="Buyruqni",
                 correct_option='c'),
        Question(lesson=kochirma, text="'Ali gelmiş' iborasining ma'nosi?",
                 option_a="Ali keladi", option_b="Ali kelgan ekan", option_c="Ali kelsin",
                 option_d="Ali kelmoqda", correct_option='b'),
    ])

    adabiy = Lesson.objects.create(
        level=c1, order=3, title="O'qish: Adabiy parcha",
        content=(
            "TURKCHA MATN:\n"
            "\"Hayat, bazen sessizce akan bir nehir gibidir. İnsan bazen "
            "hızlanır, bazen durur, ama nehir her zaman denize doğru gitmeye "
            "devam eder. Belki de önemli olan hızımız değil, doğru yönde "
            "ilerlememizdir.\"\n\n"
            "O'ZBEKCHA TARJIMASI:\n"
            "\"Hayot ba'zan sokin oqayotgan daryoga o'xshaydi. Inson ba'zan "
            "tezlashadi, ba'zan to'xtaydi, lekin daryo doim dengiz tomon "
            "oqishda davom etadi. Balki muhimi tezligimiz emas, to'g'ri "
            "yo'nalishda harakatlanishimizdir.\"\n\n"
            "Bu — hayot haqidagi kichik falsafiy mulohaza. Matndagi "
            "metafora (o'xshatish) nimani anglatishi haqida o'ylab ko'ring."
        ),
    )
    VocabularyWord.objects.bulk_create([
        VocabularyWord(lesson=adabiy, order=1, turkish="Nehir", uzbek="Daryo"),
        VocabularyWord(lesson=adabiy, order=2, turkish="Hızlanmak", uzbek="Tezlashmoq"),
        VocabularyWord(lesson=adabiy, order=3, turkish="Yön", uzbek="Yo'nalish"),
        VocabularyWord(lesson=adabiy, order=4, turkish="İlerlemek", uzbek="Ilgarilamoq/harakatlanmoq"),
    ])
    Question.objects.bulk_create([
        Question(lesson=adabiy, text="Matnda hayot nimaga o'xshatilgan?",
                 option_a="Dengizga", option_b="Nehirga (daryoga)", option_c="Tog'ga",
                 option_d="Osmonga", correct_option='b'),
        Question(lesson=adabiy, text="Matn muallifi fikricha, muhim bo'lgan narsa nima?",
                 option_a="Tezlik", option_b="To'g'ri yo'nalishda harakatlanish",
                 option_c="Kuch", option_d="Pul", correct_option='b'),
    ])

    # ==================================================================
    # Yakuniy imtihon havzasiga qo'shimcha savollar
    # ==================================================================
    Question.objects.bulk_create([
        Question(lesson=None, text="Turk alifbosida nechta harf bor?",
                 option_a="26", option_b="29", option_c="30", option_d="33", correct_option='b'),
        Question(lesson=None, text="'Ç' harfi qanday tovush beradi?",
                 option_a="'j'", option_b="'ch'", option_c="'sh'", option_d="'k'", correct_option='b'),
        Question(lesson=None, text="Turk tilida so'zlarda urg'u odatda qayerga tushadi?",
                 option_a="Birinchi bo'g'inga", option_b="Oxirgi bo'g'inga",
                 option_c="Ikkinchi bo'g'inga", option_d="Urg'u bo'lmaydi", correct_option='b'),
        Question(lesson=None, text="'Bormoq' fe'lining turkchasi?",
                 option_a="Gelmek", option_b="Gitmek", option_c="Yapmak", option_d="Görmek",
                 correct_option='b'),
        Question(lesson=None, text="Kelasi zamon qo'shimchasi qaysi?",
                 option_a="-di", option_b="-ecek/-acak", option_c="-yor", option_d="-miş",
                 correct_option='b'),
        Question(lesson=None, text="'Eli açık' iborasi nimani anglatadi?",
                 option_a="Saxiy odam", option_b="Xasis odam", option_c="G'azabli odam",
                 option_d="Charchagan odam", correct_option='a'),
        Question(lesson=None, text="Majhul nisbat qanday yasaladi?",
                 option_a="-il/-in qo'shimchasi bilan", option_b="-ecek qo'shimchasi bilan",
                 option_c="-di qo'shimchasi bilan", option_d="-yor qo'shimchasi bilan",
                 correct_option='a'),
        Question(lesson=None, text="'-mış/-miş' qo'shimchasi nimani bildiradi?",
                 option_a="Buyruqni", option_b="Kelasi zamonni",
                 option_c="Eshitilgan/bilvosita ma'lumotni", option_d="Savolni", correct_option='c'),
        Question(lesson=None, text="'Geldim' so'zining ma'nosi?",
                 option_a="Kelaman", option_b="Keldim", option_c="Kelasan", option_d="Kelgin",
                 correct_option='b'),
        Question(lesson=None, text="'I' (nuqtasiz) harfi haqida to'g'ri fikr qaysi?",
                 option_a="Oddiy 'i' kabi aytiladi", option_b="'ы' ga o'xshash tovush beradi",
                 option_c="Umuman aytilmaydi", option_d="'u' kabi aytiladi", correct_option='b'),
    ])


def remove_advanced_content(apps, schema_editor):
    Level = apps.get_model('courses', 'Level')
    Lesson = apps.get_model('courses', 'Lesson')

    Level.objects.filter(code__in=['B2', 'C1']).delete()
    Lesson.objects.filter(title__in=[
        "Turk alifbosi", "Talaffuz qoidalari", "O'qish: Yangi tanish",
        "O'tgan zamon (-di)", "O'qish: Sayohat kundaligi",
    ]).delete()

    Question = apps.get_model('courses', 'Question')
    Question.objects.filter(
        lesson__isnull=True,
        text__in=[
            "Turk alifbosida nechta harf bor?", "'Ç' harfi qanday tovush beradi?",
            "Turk tilida so'zlarda urg'u odatda qayerga tushadi?",
            "'Bormoq' fe'lining turkchasi?", "Kelasi zamon qo'shimchasi qaysi?",
            "'Eli açık' iborasi nimani anglatadi?", "Majhul nisbat qanday yasaladi?",
            "'-mış/-miş' qo'shimchasi nimani bildiradi?", "'Geldim' so'zining ma'nosi?",
            "'I' (nuqtasiz) harfi haqida to'g'ri fikr qaysi?",
        ],
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_more_lessons'),
    ]

    operations = [
        migrations.RunPython(seed_advanced_content, remove_advanced_content),
    ]
