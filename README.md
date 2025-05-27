# Python-Grup-Projesi

## Müşteri Memnuniyeti Tahmin Sistemi - Proje Raporu

### 1. Giriş

Bu proje, müşteri memnuniyetini tahmin etmek amacıyla geliştirilmiş bir makine öğrenmesi tabanlı sistemdir. Proje kapsamında, farklı algoritmalarla dört farklı model eğitilmiş ve kullanıcıdan alınan verilerle müşterinin memnun olup olmayacağı tahmin edilmiştir.

### 2. Veri ve Özellikler

Projede kullanılan veriler; yaş, cinsiyet, hizmet kalitesi, bekleme süresi, temizlik, menü çeşitliliği, lezzet kalitesi ve fiyat gibi değişkenleri içermektedir. Bu veriler kullanıcı girişleri ile elde edilmekte ve daha sonra makine öğrenmesi modelleri ile değerlendirilerek tahmin yapılmaktadır.

### 3. Kullanılan Modeller

Proje ekibindeki her üye farklı bir makine öğrenmesi algoritmasıyla model geliştirmiştir:

* Lojistik Regresyon
* Destek Vektör Makineleri (SVM)
* Karar Ağaçları
* Naive Bayes

Her model kendi içinde değerlendirilmiş, doğruluk skorlarına göre karşılaştırılmış ve final model olarak lojistik regresyon seçilmiştir.

### 4. Model Seçimi ve Gerekçe

SVM modeli doğruluk açısından başarılı sonuçlar vermiş olsa da, Logistic Regression modeli; daha yorumlanabilir olması, daha hızlı çalışması ve genelleme yeteneği açısından avantajlı bulunmuştur. Bu nedenle son kullanıcıya sunulan arayüzde Logistic Regression kullanılmıştır.

### 5. Arayüz ve Kullanım

Projede Flask framework’ü kullanılarak basit bir web arayüzü geliştirilmiştir. Kullanıcılar yaş, cinsiyet ve hizmet puanlarını girerek sistemden tahmin alabilmektedir. Ayrıca sistem, müşterinin en memnun ve en memnun kalmadığı alanları da geri bildirim olarak sunmaktadır.

### 6. Sonuç

Bu proje sayesinde ekip üyeleri farklı makine öğrenmesi algoritmalarını pratik bir şekilde öğrenmiş ve karşılaştırmıştır. Ayrıca web uygulaması entegrasyonu ile teorik bilgiler uygulamaya dökülmüştür. Sistem, kullanıcı dostu yapısıyla müşteri memnuniyeti analizinde etkili bir araç olmayı hedeflemektedir.

### 7. Proje Geliştiricileri

* **Semanur Erdoğan** - 032390064
* **Sevim Çıra** - 032390053
* **Neslihan Özdemir** - 032390069
* **Buse Yılmaz** - 032390024
