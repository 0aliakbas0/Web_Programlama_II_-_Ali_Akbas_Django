# CyberPoll - Siber Güvenlik Anketi Merkezi

Bu proje, orijinal Django "Polls" eğitim uygulamasının geliştirilerek tamamen modern ve kurumsal bir **"Siber Güvenlik Değerlendirme ve Zafiyet Anketi"** sistemine dönüştürülmüş halidir.

Proje, standart anket yapısını alıp Bootstrap 5 ve özel CSS/JS (Glassmorphism, Parallax arka planlar, akıcı sayaç animasyonları) ile destekleyerek birinci sınıf (premium) bir kullanıcı deneyimi sunmayı hedefler.

## Projeyi Çalıştırma Rehberi

Projeyi kendi bilgisayarınızda (lokalde) çalıştırmak için aşağıdaki adımları izleyin:

### Gerekli Kurulumlar
- Python (3.x sürümü) yüklü olmalıdır.
- Django yüklü olmalıdır (`pip install django`).

### Adımlar
1. Terminal veya Komut İstemini (CMD) açın.
2. Projenin ana klasörüne (`manage.py` dosyasının bulunduğu dizine) gidin.
3. Veritabanını hazırlamak ve mevcut tablo yapılarını uygulamak için:
   ```bash
   python manage.py migrate
   ```
4. Geliştirme sunucusunu başlatmak için aşağıdaki komutu girin:
   ```bash
   python manage.py runserver
   ```
5. Tarayıcınızı açın ve sistemi test edin:
   - **Ana Sayfa (Otomatik Yönlendirmeli):** `http://127.0.0.1:8000/` veya `http://127.0.0.1:8000/polls/`
   - **Yönetici (Admin) Paneli:** `http://127.0.0.1:8000/admin/`

*(Admin paneli üzerinden yeni anketler eklemek için `python manage.py createsuperuser` komutunu kullanarak bir yönetici hesabı oluşturabilirsiniz.)*

---

## Projede Yapılan Modifikasyonlar ve Yenilikler (Vize/Final Teslimi İçin)

Proje, salt olarak eğitimdeki haliyle bırakılmayıp aşağıdaki geliştirmelerle zenginleştirilmiştir:

### 1. Premium UI/UX ve Modern Arayüz (Glassmorphism)
- Orijinal düz liste yapıları yerine, modern "Glassmorphism" teknolojisi (buzlu cam görünümü ve blur efektleri) kullanılarak kartlar ve menüler oluşturulmuştur.
- Animasyonlu gradient arka planlar ve mouse hareketine duyarlı (parallax) gezinen küre (orb) nesneleri eklenmiştir.
- Sonuç ekranlarında JS destekli sayaçlar, renkli yüzdelik ilerleme (progress) çubukları ve etkileşimli "confetti" patlama efektleri yer almaktadır.

### 2. Kavramsal Değişim: Siber Güvenlik Teması
- Uygulama basit anketlerden öte, kurumsal şirketlerin siber güvenlik politikalarını ve güvenlik zafiyetlerini personeline oylattığı profesyonel bir araca (CyberPoll) dönüştürülmüştür.
- İkon olarak Bootstrap Icons kütüphanesine ait güvenlik kalkanları, şifre ve grafik simgeleri tercih edilmiştir.

### 3. Otomatik URL Yönlendirmesi
- Kullanıcılar ana sayfa dizinine (`/`) girdiklerinde `RedirectView` kullanılarak otomatik olarak anketlerin olduğu (`/polls/`) dizinine aktarılmaktadır.
- Oylama işlemindeki mantıksal yüzdelik hesaplamalar tamamen Django'nun `views.py` dosyası üzerinden handle edilerek şablona beslenmiştir.
