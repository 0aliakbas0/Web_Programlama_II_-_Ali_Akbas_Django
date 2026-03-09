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

Mesut Hoca'nın "Backend dahil tam çalışan, modifiye edilmiş sürüm olacak" beklentisi doğrultusunda projede yapılacak geliştirmeler şunlardır:

### 1. Tasarım ve Kullanıcı Arayüzü (UI) İyileştirmeleri
- Düz HTML sayfaları yerine **Bootstrap** framework'ü entegre edilecek.
- Anket listesi şık **kart (card)** yapılarına dönüştürülecek.
- Oy verme ekranı ve sonuçlar ekranı modern butonlar, renkli temalar ve hover efektleriyle zenginleştirilecek.

### 2. Oylama Sistemi Modifikasyonları
- "Polls" (Anketler) konsepti, **"Teknofest Proje Oylama Sistemi"** veya benzeri kurumsal bir yapıya çevrilecek. 
- Soru ve şık ekleme ekranları (Admin paneli haricinde, eğer gerekirse) geliştirilecek.
- Sonuç sayfasında oy oranları sadece düz rakam olarak değil, **renkli ilerleme çubukları (Progress Bars)** ve yüzdelik dilimlerle görselleştirilecek.

### 3. Kullanıcı Deneyimi (UX) ve Yönlendirmeler
- Ana sayfa (`/`) rotası boş bırakılıp 404 hatası vermek yerine, doğrudan `/polls/` (Oylama Listesi) sayfasına yönlendirilecek.
- Sayfalar arası geçişlerde "Geri Dön", "Tekrar Oy Ver" gibi navigasyon butonları daha belirgin hale getirilecek.
- (İsteğe bağlı) Sadece kayıtlı veya giriş yapmış kullanıcıların oy verebilmesi özelliği eklenebilir.
