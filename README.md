# Teknofest Proje Fikri Oylama Sistemi (Django Tutorial Modifikasyonu)

Bu proje, orijinal [Django 8 Parçalı Eğitimi'nin (Polls App)](https://docs.djangoproject.com/en/5.1/intro/tutorial01/) temel alınarak geliştirilmiş ve Teknofest projeleri, etkinlikleri veya genel oylamalar için modifiye edilecek olan bir web uygulamasıdır.

Şu anki ilk sürüm, eğitimin orijinal **değiştirilmemiş** halidir.

---

## Projeyi Çalıştırma Rehberi

Projeyi kendi bilgisayarınızda (lokalde) çalıştırmak için aşağıdaki adımları izleyin:

### Gerekli Kurulumlar
- Python (3.x sürümü) yüklü olmalıdır.
- Django yüklü olmalıdır (`pip install django`).

### Adımlar
1. Terminal veya Komut İstemini (CMD) açın.
2. Projenin ana klasörüne (`manage.py` dosyasının bulunduğu dizine) gidin.
3. Veritabanını hazırlamak ve mevcut tablo yapılarını uygulamak için (ilk kez çalıştırılıyorsa):
   ```bash
   python manage.py migrate
   ```
4. Geliştirme sunucusunu başlatmak için aşağıdaki komutu girin:
   ```bash
   python manage.py runserver
   ```
5. Tarayıcınızı açın ve şu adreslere gidin:
   - **Anketler (Polls) Sayfası:** `http://127.0.0.1:8000/polls/`
   - **Yönetici (Admin) Paneli:** `http://127.0.0.1:8000/admin/`

*(Admin paneli için eğer bir süper kullanıcı hesabı oluşturmadıysanız, `python manage.py createsuperuser` komutunu kullanarak oluşturabilirsiniz.)*

---

## Gelecek Planları ve Modifikasyon Hedefleri

Mesut Hoca'nın "Backend dahil tam çalışan, modifiye edilmiş sürüm olacak" beklentisi doğrultusunda projede yapılacak tüm geliştirmeler **tamamen Django altyapısı ve özellikleri kullanılarak** gerçekleştirilecektir.

### 1. Django Temelli Tasarım İyileştirmeleri
- Orijinal düz HTML sayfaları, **Django Şablon Motoru (Template Engine)** kullanılarak daha dinamik ve şık tasarımlara (Bootstrap ile desteklenerek) entegre edilecektir. 
- Harici bir önyüz framework'ü kullanılmadan, sayfa render işlemleri tamamen Django `views` (görünümler) üzerinden yapılacaktır.

### 2. Oylama Sistemi Modifikasyonları (Django ORM ve Views)
- "Polls" (Anketler) konsepti, **"Teknofest Proje Oylama Sistemi"** yapısına çevrilecek ve bu kapsamda **Django Modelleri (Models)** üzerinde gerekli veritabanı ayarlamaları yapılacaktır.
- Oylama sonuçlarının hesaplanması ve ekrana basılması işlemleri tamamen **Django ORM**'in güçlü sorgu yetenekleriyle (F ifadeleri vb.) yönetilecektir.

### 3. Kullanıcı Deneyimi (UX) ve Yönlendirmeler
- Ana sayfa (`/`) rotası, `urls.py` içerisinde bir `RedirectView` kullanılarak doğrudan `/polls/` (Oylama Listesi) sayfasına yönlendirilecektir.
- Gelecek planları arasında sisteme giriş/çıkış entegrasyonu bulunursa, bu da tamamen **Django'nun yerleşik yetkilendirme (Authentication)** sistemi üzerinden kurgulanacaktır.
