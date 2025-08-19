# 📝 SQLite Web Uygulaması

Bu proje, **Flask** ve **SQLite** kullanılarak geliştirilmiş basit bir web uygulamasıdır.  
Kullanıcı ekleme, kullanıcıları listeleme ve admin paneli ile veritabanı tablolarını görselleştirme özelliklerine sahiptir.

---

## 🚀 Özellikler

- Kullanıcı ekleme (`/add`)
- Kullanıcıları listeleme (`/users`)
- Admin paneli ile tüm veritabanı tablolarını görme (`/admin`)
- Modern ve basit bir arayüz (HTML + CSS)

---

## 📂 Dosya Yapısı

```
MySite/
├── app.py          # Flask uygulaması
├── database.db     # SQLite veritabanı dosyası
├── schema.sql      # Veritabanı tablo şeması
├── README.md       # Proje açıklaması
├── templates/      # HTML şablonları
│   ├── index.html
│   ├── add.html
│   ├── users.html
│   └── admin.html
└── static/         # CSS dosyaları
    └── style.css
```

---

## 🔧 Kurulum

1. Gerekli kütüphaneleri yükleyin:

   ```bash
   pip install flask
   ```

2. Projeyi çalıştırın:

   ```bash
   python app.py
   ```

3. Tarayıcıdan açın:
   ```
   http://127.0.0.1:5000/
   ```

---

## 📊 Sayfalar

- `/` → Ana sayfa
- `/add` → Yeni kullanıcı ekleme
- `/users` → Kayıtlı kullanıcılar listesi
- `/admin` → Veritabanı tablolarını görüntüleme paneli

---

## 🔮 Geliştirme Fikirleri

- Kullanıcı silme ve güncelleme özellikleri
- Giriş sistemi (admin login)
- Daha modern bir arayüz (Bootstrap / Tailwind)

---

👨‍💻 **Yasin Adıgüzel** ile hazırlanmıştır.
