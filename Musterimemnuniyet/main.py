import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def main():
    # 1) CSV dosyasını oku
    df = pd.read_csv("Python_Veriler_400_ortalamasiz.csv", encoding="utf-8")

    # 2) Cinsiyet sayısal değilse dönüştür
    if df["Cinsiyet"].dtype == object:
        df["Cinsiyet"] = (
            df["Cinsiyet"]
              .str.strip()
              .str.lower()
              .map({"erkek": 0, "kadın": 1})
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
    yas = int(input("Yaş: "))
    cinsiyet = input("Cinsiyet (erkek/kadın): ").strip().lower()
    cinsiyet = 0 if cinsiyet == "erkek" else 1
    hizmet = int(input("Hizmet Kalitesi (1-10): "))
    bekleme = int(input("Bekleme Süresi (1-10): "))
    temizlik = int(input("Temizlik (1-10): "))
    menu = int(input("Menü Çeşitliliği (1-10): "))
    lezzet = int(input("Lezzet Kalitesi (1-10): "))
    fiyat = int(input("Fiyat Uygunluğu (1-10): "))

    yeni_veri = pd.DataFrame([[yas, cinsiyet, hizmet, bekleme, temizlik, menu, lezzet, fiyat]],
                              columns=özellikler)

    tahmin = model.predict(yeni_veri)[0]
    print("\nTahmin:", "Memnun kalır 👍" if tahmin == 1 else "Memnun kalmaz 👎")

if __name__ == "__main__":
    main()
