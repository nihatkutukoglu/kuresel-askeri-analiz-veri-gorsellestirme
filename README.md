

### \# Global Military Power Analysis & Visualization

Bu proje, Global Firepower verilerini kullanarak 133 ülkenin askeri güç metriklerini derinlemesine analiz eden ve görselleştiren kapsamlı bir çalışmadır. Amaç, savunma bütçesi, personel sayısı, ekonomik güç (PPP) ve askeri varlıklar (Hava, Kara, Deniz) arasındaki karmaşık ilişkileri ortaya çıkarmaktır.

### ✨ Anahtar Analiz Alanları

Projeyi derinleştiren ve öne çıkaran dört ana görsel analiz yapılmıştır:

1.  **Güç Sıralaması:** En yüksek savunma bütçesine ve toplam askeri personele sahip 10 ülkenin karşılaştırması.
2.  **Varlık Korelasyonu (Heatmap):** Savunma bütçesi ile uçak, tank ve deniz varlıkları arasındaki doğrusal ilişkinin incelenmesi.
3.  **Ekonomik Etki:** Askeri sıralama (`Rank`) ile ülkenin ekonomik büyüklüğü (`PPP`) arasındaki güçlü negatif korelasyonun serpilme grafiği (`Scatter Plot`) ile kanıtlanması.
4.  **Varlık Dağılımı:** En güçlü 5 ülkenin Hava, Kara ve Deniz kuvvetlerindeki varlıklarının logaritmik ölçekte karşılaştırmalı analizi.

### 🛠️ Teknolojiler

| Kütüphane | Rolü |
| :--- | :--- |
| **Pandas** | Veri yükleme, temizleme, normalleştirme (`Defense Budget` ve `Total Military Personnel` metriklerini Milyar/Milyon birimlerine çevirme) ve alt kümeleme işlemleri. |
| **Numpy** | Pandas operasyonlarının temelinde yer alan sayısal işlemler ve hesaplamalar. |
| **Matplotlib & Seaborn** | Yüksek kaliteli, bilgi açısından zengin ve Türkçe karakter uyumlu (font ayarı yapılmıştır) tüm görselleştirmelerin oluşturulması. |

### 🚀 Kurulum ve Çalıştırma

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları takip edin:

#### Ön Gereksinimler

Bu projeyi çalıştırmak için Python 3.x kurulu olmalıdır. Gerekli kütüphaneleri yükleyin:

```bash
pip install pandas numpy matplotlib seaborn
```

#### Çalıştırma Adımı

1.  **`GLOBAL_FIREPOWER.CSV`** dosyasını proje klasörüne kopyalayın.
2.  Ana Python dosyasını çalıştırın:

<!-- end list -->

```bash
python military_analysis_project.py
```

Kod çalıştıktan sonra, tüm analiz çıktılarını konsolda görecek ve dört farklı grafik otomatik olarak ekranda belirecektir.

### 📂 Dosya Yapısı

```
.
├── GLOBAL_FIREPOWER.CSV  # Analiz edilen ham veri
├── military_analysis_project.py  # Tek akışlı, fonksiyonsuz ana analiz kodu
└── README.md
```

### 🤝 Katkıda Bulunma

Proje açıktır ve katkılarınızı bekler. Yeni analizler veya daha gelişmiş görselleştirme teknikleri önermek isterseniz, lütfen bir "Issue" açın veya "Pull Request" gönderin.

-----

**Not:** Bu proje, veri bilimi ve görselleştirme tekniklerini sergilemek amacıyla hazırlanmıştır.
