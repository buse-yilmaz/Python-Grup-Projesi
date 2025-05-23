import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def girdi_al(mesaj, min_deger=1, max_deger=10):
    while True:
        try:
            deger = int(input(mesaj))
            if min_deger <= deger <= max_deger:
                return deger
            else:
                print(f"Lütfen {min_deger}-{max_deger} arasında bir değer girin.")
        except ValueError:
            print("Sadece sayı giriniz.")

def cinsiyet_al():
    while True:
        giris = input("Cinsiyet (erkek/kadın ya da 0/1): ").strip().lower()
        if giris in ["erkek", "0"]:
            return 0
        elif giris in ["kadın", "1", "kadin"]:
            return 1
        else:
            print("Geçerli bir cinsiyet girin (erkek/kadın ya da 0/1)")

def main():
    # 1) CSV dosyasını oku
    df = pd.read_csv("Python_Veriler_400_ortalamasiz.csv", encoding="utf-8")

    # 2) Cinsiyet sayısal değilse dönüştür
    if df["Cinsiyet"].dtype == object:
        df["Cinsiyet"] = (
            df["Cinsiyet"]
              .str.strip()
              .str.lower()
              .map({"erkek": 0, "kadın": 1, "kadin": 1})
        )

    # 3) Eksik verileri temizle
    df = df.dropna()

    # 4) Giriş ve çıkış verileri
    özellikler = ["Yaş", "Cinsiyet", "Hizmet Kalitesi", "Bekleme Süresi",
                  "Temizlik", "Menü Çeşitliliği", "Lezzet Kalitesi", "Fiyat"]
    X = df[özellikler]
    y = df["Memnuniyet"]

    # 5) Veriyi eğitim/test olarak ayır
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 6) Modeli eğit
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # 7) Doğruluk yazdır
    y_pred = model.predict(X_test)
    print("Model doğruluğu:", accuracy_score(y_test, y_pred))

    # 8) Kullanıcıdan veri al ve tahmin yap
    print("\nLütfen aşağıdaki bilgileri girin:")
    yas = girdi_al("Yaş (18-65): ", min_deger=18, max_deger=65)
    cinsiyet = cinsiyet_al()
    hizmet = girdi_al("Hizmet Kalitesi (1-10): ")
    bekleme = girdi_al("Bekleme Süresi (1-10): ")
    temizlik = girdi_al("Temizlik (1-10): ")
    menu = girdi_al("Menü Çeşitliliği (1-10): ")
    lezzet = girdi_al("Lezzet Kalitesi (1-10): ")
    fiyat = girdi_al("Fiyat Uygunluğu (1-10): ")

    yeni_veri = pd.DataFrame([[yas, cinsiyet, hizmet, bekleme, temizlik, menu, lezzet, fiyat]],
                             columns=özellikler)

    tahmin = model.predict(yeni_veri)[0]
    print("\nTahmin:", "Memnun kalır 👍" if tahmin == 1 else "Memnun kalmaz 👎")

    # 9) En yüksek ve en düşük puanı bul
    puanlar = {
        "Hizmet Kalitesi": hizmet,
        "Bekleme Süresi": bekleme,
        "Temizlik": temizlik,
        "Menü Çeşitliliği": menu,
        "Lezzet Kalitesi": lezzet,
        "Fiyat Uygunluğu": fiyat
    }

    en_memnun = max(puanlar, key=puanlar.get)
    en_memnun_deg = puanlar[en_memnun]

    en_memnun_degil = min(puanlar, key=puanlar.get)
    en_memnun_degil_deg = puanlar[en_memnun_degil]

    print(f"\n💚 En memnun olduğu kısım: {en_memnun} ({en_memnun_deg}/10)")
    print(f"💔 En az memnun olduğu kısım: {en_memnun_degil} ({en_memnun_degil_deg}/10)")


if __name__ == "__main__":
    main()