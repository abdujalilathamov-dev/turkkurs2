# Türkçe.Kurs — Turk Tili O'quv Platformasi 🎓

Abdujalil uchun tayyorlangan — Turk tilini bosqichma-bosqich o'rgatuvchi,
har bir darsdan keyin test topshiriladigan, barcha darslar tugagach yakuniy
imtihon va rasmiy sertifikat beriladigan to'liq Django platforma.
Dizayn: zamonaviy **dark / neon** uslub, havo-rang (sky blue) neon banner bilan.

## Xususiyatlar

- 🎨 Zamonaviy **dark mode / neon** dizayn — havo-rang porlab turuvchi xush kelibsiz banneri
- 📚 **5 ta daraja** — A1, A2, B1, B2, C1 (CEFR standartiga mos, Boshlang'ichdan Ilg'origacha)
- 🔤 **Alifbo va talaffuz qoidalari** — turk alifbosi, maxsus harflar, unlilar uyg'unligi
- 📖 **O'qish matnlari** — har darajada haqiqiy matn (turkcha + o'zbekcha tarjima) va tushunish testlari
- 📐 **Grammatika darslari** — o'tgan/kelasi zamon, majhul nisbat, ko'chirma gap va boshqalar
- 💬 Idiomalar va jonli iboralar (yuqori darajalarda)
- 📖 Har bir darsda tushuntirish matni + lug'at (turkcha—o'zbekcha so'zlar)
- 📝 Har bir dars oxirida test (4 variantli savollar, 60% o'tish balli)
- 🎓 **Yakuniy imtihon** — barcha darslar tugagach ochiladi, tasodifiy savollar, 70% o'tish balli
- 🏆 **Avtomatik sertifikat** — imtihondan o'tgach, noyob raqamli rasmiy sertifikat (chop etish/PDF saqlash imkoniyati bilan)
- 🔍 **Ochiq sertifikat tekshiruvi** — har kim sertifikat raqami bilan uning haqiqiyligini tekshira oladi (kirishsiz)
- 🏅 Jamoaviy reyting — eng faol talabalar
- 🛠 **Kuchli admin panel**: talabalar statistikasi, bugungi faollik, berilgan sertifikatlar, imtihondan o'tish foizi, to'liq reyting
- 📱 Boshidanoq mobil qurilmalarga moslashtirilgan
- ✅ 5 ta daraja, 21 ta dars (alifbo, talaffuz, grammatika, o'qish matnlari, idiomalar), boy lug'at va test savollari bilan **tayyor namuna kontent** o'rnatilgandan so'ng darhol ishlatish uchun qo'shilgan

## O'rnatish va ishga tushirish (Windows)

> Eslatma: `pip` o'rniga har doim `python -m pip` ishlating.

**1. Zip faylni chiqaring va to'g'ri papkaga kiring**

Explorer'da zip faylni **"Extract All"** orqali chiqaring. Ichidagi `turkkurs` papkasini oching — `manage.py` fayli ko'rinib turgan joyda bo'sh joyga Shift bosib turib o'ng tugma → **"Open in Terminal"**.

**2. Kerakli kutubxonani o'rnating**

```bat
python -m pip install -r requirements.txt
```

**3. Ma'lumotlar bazasini tayyorlang**

```bat
python manage.py migrate
```

Bu buyruq ishga tushganda, 5 ta daraja (A1—C1), 21 ta dars — jumladan alifbo, talaffuz qoidalari, grammatika va o'qish matnlari — avtomatik qo'shiladi.

> **Diqqat:** agar avvalgi versiyadan yangilayotgan bo'lsangiz, darslar soni ko'paygani uchun mavjud foydalanuvchilarning "imtihonga tayyorlik" foizi qaytadan hisoblanadi — ular yangi qo'shilgan darslarni ham tugatishlari kerak bo'ladi.

**4. Admin hisobini yarating**

```bat
python manage.py createsuperuser
```

**5. Serverni ishga tushiring**

```bat
python manage.py runserver
```

Brauzerda oching:
- Platforma: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

## Yangi dars/daraja qanday qo'shiladi

1. `/admin/` ga kiring
2. **Darajalar** bo'limida yangi daraja qo'shing (masalan "Yuqori — B1")
3. **Darslar** bo'limida yangi dars qo'shing, darajasini tanlang, matn yozing
4. Pastdagi **"Lug'at so'zlari"** va **"Test savollari"** bo'limlaridan kerakli miqdorda qo'shing
5. Yakuniy imtihon savollari uchun — **Test savollari** bo'limida yangi savol qo'shganda **"Dars"** maydonini bo'sh qoldiring — bu savol avtomatik imtihon havzasiga tushadi

## Windows'da tez-tez chiqadigan xatoliklar

**"execution of scripts is disabled" (PowerShell)** — Command Prompt (cmd.exe) dan foydalaning yoki `venv\Scripts\activate.bat` deb yozing.

**"Политика управления приложениями заблокировала этот файл" (pip.exe bloklangan)** — `pip install` o'rniga:
```bat
python -m pip install -r requirements.txt
```

**"can't open file 'manage.py'"** — Terminal noto'g'ri papkada. `dir` bilan tekshiring, `manage.py` ko'rinib turgan papkada bo'lishingiz kerak.

**Telefondan kirish uchun**: `python manage.py runserver 0.0.0.0:8000` bilan ishga tushiring, kompyuteringiz IP-manzilini (`ipconfig`) toping, telefon bilan bir xil Wi-Fi'da bo'lib `http://<IP>:8000` ni oching.

## Keyingi qadamlar uchun g'oyalar

- Sertifikatni haqiqiy PDF fayl sifatida yuklab olish (weasyprint yoki shunga o'xshash kutubxona bilan)
- Audio talaffuz — lug'at so'zlariga ovoz fayli qo'shish
- Telegram bot orqali kunlik so'z eslatmasi
- Video darslarni to'g'ridan-to'g'ri sahifada ko'rsatish (YouTube embed)

## Google orqali kirish (talabalar uchun sodda ro'yxatdan o'tish)

Talabalar email/parol yozishga qiynalmasligi uchun **"Google orqali kirish"**
tugmasi qo'shildi. Buni ishlatish uchun bir marta sozlash kerak:

**1-qadam: Google Cloud Console'da OAuth ma'lumotlarini yarating**
- https://console.cloud.google.com/ ga kiring, yangi loyiha yarating (yoki mavjudini tanlang)
- **"APIs & Services" → "OAuth consent screen"** ga o'ting, **External** turini tanlang, ilova nomi va emailingizni kiriting, saqlang
- **"APIs & Services" → "Credentials" → "Create Credentials" → "OAuth client ID"**
- Turi: **Web application**
- **Authorized redirect URIs** ga aynan shuni qo'shing (o'z domeningiz bilan):
  ```
  https://sizning-saytingiz.onrender.com/social/google/login/callback/
  ```
- **Create** tugmasini bosing — sizga **Client ID** va **Client Secret** beriladi

**2-qadam: Render'da muhit o'zgaruvchilarini qo'shing**
```
GOOGLE_CLIENT_ID=sizning-client-id
GOOGLE_CLIENT_SECRET=sizning-client-secret
```

**3-qadam: Saytingiz domenini Django admin'da to'g'irlang**

Deploy qilingandan so'ng, `/admin/sites/site/1/change/` sahifasiga kiring va:
- **Domain name**: `sizning-saytingiz.onrender.com`
- **Display name**: `Türkçe.Kurs`

qilib saqlang. Bu — Google login to'g'ri manzilga qaytishi uchun **shart**.

**4-qadam: Sinab ko'ring**

Kirish yoki ro'yxatdan o'tish sahifasida **"Google orqali kirish"** tugmasini bosing — talaba o'zining mavjud Google hisobini tanlaydi, **"Davom etish"** bosadi va darhol tizimga kiritiladi, hech qanday parol kiritmasdan.

## Render'ga joylashtirish (deploy) — muhim!

### Muammo: nega admin panelga kira olmayapman?

Render'ning **bepul** serverlarida disk **vaqtinchalik** — har safar server qayta ishga tushganda `db.sqlite3` fayli **tozalanib ketadi**, shu bilan birga yaratgan superuser hisobingiz ham yo'qoladi. Shuning uchun `/admin/` ga kirolmaysiz, ro'yxatdan o'tsangiz esa oddiy talaba bo'lib qoladi.

### Yechim: Render PostgreSQL'ga ulanish (bir marta sozlanadi, doimiy ishlaydi)

**1-qadam: Render'da bepul PostgreSQL yarating**
- Render Dashboard → **New** → **PostgreSQL** → nomini bering → **Free** rejani tanlang → **Create Database**
- Yaratilgach, **"Internal Database URL"** qatorini nusxa oling

**2-qadam: Web Service'ingizga ulang**
- Web service (saytingiz) sozlamalariga o'ting → **Environment** bo'limi
- Yangi environment variable qo'shing: `DATABASE_URL` = (1-qadamda nusxa olgan Internal Database URL)

**3-qadam: Superuser'ni avtomatik yaratish uchun yana muhit o'zgaruvchilari qo'shing**
```
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=kuchli-parol-shu-yerga
```

**4-qadam: Build Command'ni yangilang**

Render'dagi **Build Command** maydoniga shuni yozing (bitta qatorda, `&&` bilan):
```bash
pip install -r requirements.txt && python manage.py migrate && python manage.py createsuperuser --noinput || true
```

`|| true` qismi — agar superuser allaqachon mavjud bo'lsa, build to'xtab qolmasligi uchun kerak.

**5-qadam: Qayta deploy qiling**

Render avtomatik ravishda: PostgreSQL'ga ulanadi (bazangiz endi doimiy saqlanadi) → migratsiyalarni ishga tushiradi → sizning `DJANGO_SUPERUSER_*` ma'lumotlaringiz bilan superuser yaratadi.

Shundan keyin `https://sizning-saytingiz.onrender.com/admin/` ga o'sha login/parol bilan **doimiy** kira olasiz — keyingi deploy'larda ham hisobingiz yo'qolmaydi.

> **Diqqat:** `DJANGO_SUPERUSER_PASSWORD`ni hech kimga ko'rsatmang va oddiy so'zlardan foydalanmang.

## Production'ga chiqarishdan oldin

`turkkurs/settings.py` faylida `DEBUG = False` qiling, `SECRET_KEY`ni maxfiy
qiymatga almashtiring va `ALLOWED_HOSTS`ga domeningizni kiriting.

