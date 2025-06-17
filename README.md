# 🐎 TayinApp - Yarış Atı Performans Tahmin Sistemi

TayinApp, yarış atlarının geçmiş performans verilerine göre tahminlerde bulunan bir yapay zekâ destekli analiz platformudur.

## 🚀 Özellikler
- Kullanıcı kayıt ve giriş sistemi (JWT Authentication)
- At ekleme ve listeleme
- Yarış performansı istatistiklerinin veritabanına eklenmesi
- Yapay zekâ destekli sıralama tahmini (RandomForest)
- Swagger UI üzerinden test edilebilir API

## 🛠 Kurulum
```bash
git clone https://github.com/kullaniciadi/tayinapp.git
cd tayinapp
python -m venv atintel-env
source atintel-env/bin/activate   # Windows için: .\atintel-env\Scripts\activate
pip install -r requirements.txt
