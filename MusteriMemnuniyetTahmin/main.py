import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


df = pd.read_csv("Python_Veriler_400_ortalamasiz.csv")
X = df.drop("Memnuniyet", axis=1)
y = df["Memnuniyet"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
print(f"Model Doğruluk Oranı: %{accuracy_score(y_test, y_pred) * 100:.2f}")


print("\nYeni müşteri verilerini girin. Çıkmak için 'q' yazın.\n")

while True:
    try:
        yas = input("Yaş (18-65): ")
        if yas.lower() == 'q':
            break
        yas = int(yas)
        if not (18 <= yas <= 65):
            print("Hatalı yaş. 18-65 arasında olmalı.")
            continue

        cinsiyet = input("Cinsiyet (0=Erkek, 1=Kadın): ")
        if cinsiyet.lower() == 'q':
            break
        cinsiyet = int(cinsiyet)
        if cinsiyet not in [0, 1]:
            print("Hatalı cinsiyet. 0 veya 1 olmalı.")
            continue

        def puan_al(isim):
            while True:
                val = input(f"{isim} (1-10): ")
                if val.lower() == 'q':
                    return 'q'
                try:
                    puan = int(val)
                    if 1 <= puan <= 10:
                        return puan
                    else:
                        print("1 ile 10 arasında olmalı.")
                except:
                    print("Geçerli bir sayı girin.")

        hizmet = puan_al("Hizmet Kalitesi")
        if hizmet == 'q': break
        bekleme = puan_al("Bekleme Süresi")
        if bekleme == 'q': break
        temizlik = puan_al("Temizlik")
        if temizlik == 'q': break
        menu = puan_al("Menü Çeşitliliği")
        if menu == 'q': break
        lezzet = puan_al("Lezzet Kalitesi")
        if lezzet == 'q': break
        fiyat = puan_al("Fiyat")
        if fiyat == 'q': break

        girdi = pd.DataFrame([[yas, cinsiyet, hizmet, bekleme, temizlik, menu, lezzet, fiyat]],
                             columns=X.columns)  # modelin eğitimde kullandığı sütun adları
        tahmin = model.predict(girdi)[0]

        girdi = pd.DataFrame([[yas, cinsiyet, hizmet, bekleme, temizlik, menu, lezzet, fiyat]],
                             columns=X.columns)
        tahmin = model.predict(girdi)[0]

        if tahmin == 1:
            print("\n MUSTERI MEMNUN\n")
        else:
            print("\n MUSTERI MEMNUN DEGIL\n")

        # Puanlara göre analiz
        kriterler = {
            "Hizmet Kalitesi": hizmet,
            "Bekleme Süresi": bekleme,
            "Temizlik": temizlik,
            "Menü Çeşitliliği": menu,
            "Lezzet Kalitesi": lezzet,
            "Fiyat": fiyat
        }

        en_memnun = max(kriterler, key=kriterler.get)
        en_az_memnun = min(kriterler, key=kriterler.get)

        print(f"🔹 Müşterinin en memnun olduğu alan: {en_memnun} ({kriterler[en_memnun]})")
        print(f"🔹 Müşterinin en az memnun olduğu alan: {en_az_memnun} ({kriterler[en_az_memnun]})\n")


    except Exception as e:
        print("Hata:", e)