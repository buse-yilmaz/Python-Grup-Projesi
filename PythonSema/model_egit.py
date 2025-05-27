import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle

# 1. CSV verisini oku
df = pd.read_csv("Python_Veriler_400_ortalamasiz.csv", encoding="utf-8")

# 2. Cinsiyet metinse sayıya çevir
if df["Cinsiyet"].dtype == object:
    df["Cinsiyet"] = (
        df["Cinsiyet"]
        .str.strip()
        .str.lower()
        .map({"erkek": 0, "kadın": 1, "kadin": 1})
    )

# 3. Eksik verileri sil
df = df.dropna()

# 4. Özellikleri belirle
ozellikler = [
    "Yaş", "Cinsiyet", "Hizmet Kalitesi", "Bekleme Süresi",
    "Temizlik", "Menü Çeşitliliği", "Lezzet Kalitesi", "Fiyat"
]
X = df[ozellikler]
y = df["Memnuniyet"]

# 5. Veriyi eğitim/test olarak ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Modeli oluştur ve eğit
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 7. Modeli kaydet
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ LogisticRegression modeli başarıyla eğitildi ve 'model.pkl' dosyasına kaydedildi.")
