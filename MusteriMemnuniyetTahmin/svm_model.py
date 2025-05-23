import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

# Veriyi oku
df = pd.read_csv("data/customer_data.csv")
df.columns = df.columns.str.strip().str.lower()

print("Gerçek sütun adları:")
print(df.columns.tolist())
print(df["memnuniyet"].value_counts())

# Özellik ve hedef seçimi
X = df[["yaş", "cinsiyet", "hizmet kalitesi", "bekleme süresi", "temizlik",
        "menü çeşitliliği", "lezzet kalitesi", "fiyat"]]

y = df["memnuniyet"]

# Veri bölme
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Ölçekleme (fit sadece train üzerine yapılır)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model: class_weight eklendi
model = SVC(probability=True, class_weight="balanced")
model.fit(X_train_scaled, y_train)

# Kullanıcıdan veri al
print("\n--- Müşteri Girişi ---")

while True:
    try:
        yas = int(input("Yaş (18-65): "))
        if not 18 <= yas <= 65:
            raise ValueError
        break
    except ValueError:
        print("Hatalı giriş. Yaş 18-65 arasında olmalı.")

while True:
    try:
        cinsiyet = int(input("Cinsiyet (0=kadın, 1=erkek): "))
        if cinsiyet not in [0, 1]:
            raise ValueError
        break
    except ValueError:
        print("Hatalı giriş. Cinsiyet 0 veya 1 olmalı.")

ozellikler = ["hizmet kalitesi", "bekleme süresi", "temizlik", "menü çeşitliliği", "lezzet kalitesi", "fiyat"]
puanlar = []
for oz in ozellikler:
    while True:
        try:
            puan = int(input(f"{oz} puanı (1-10): "))
            if not 1 <= puan <= 10:
                raise ValueError
            puanlar.append(puan)
            break
        except ValueError:
            print("Hatalı giriş. Puan 1 ile 10 arasında olmalı.")

# Veri çerçevesi oluştur
veri = [[yas, cinsiyet] + puanlar]
veri_df = pd.DataFrame(veri, columns=["yaş", "cinsiyet"] + ozellikler)
veri_scaled = scaler.transform(veri_df)

# Tahmin yap
tahmin = model.predict(veri_scaled)[0]
durum = "MEMNUN" if tahmin == 1 else "MEMNUN DEĞİL"

print("\n--- Tahmin Sonucu ---")
print(f"Müşteri: {durum}")

# En çok ve en az memnun kalınan alanlar
puan_serisi = pd.Series(puanlar, index=ozellikler)
en_memnun = puan_serisi.idxmax()
en_memnun_puan = puan_serisi.max()
en_az_memnun = puan_serisi.idxmin()
en_az_memnun_puan = puan_serisi.min()

print("\n--- Müşteri Geri Bildirimi ---")
print(f"✅ En memnun kalınan alan: {en_memnun.upper()} (Puan: {en_memnun_puan})")
print(f"⚠️ En az memnun kalınan alan: {en_az_memnun.upper()} (Puan: {en_az_memnun_puan})")

import joblib

# modeli kaydet
joblib.dump(model, 'svm_model.pkl')
