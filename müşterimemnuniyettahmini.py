import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

# 1. Veriyi oku
df = pd.read_csv("Python_Veriler_400_ortalamasiz.csv")

# 2. Giriş (X) ve hedef (y) değişkenlerini ayır
X = df[['Yaş', 'Cinsiyet', 'Hizmet Kalitesi', 'Bekleme Süresi', 'Temizlik',
        'Menü Çeşitliliği', 'Lezzet Kalitesi', 'Fiyat']]
y = df['Memnuniyet']

# 3. Veriyi eğitim ve test setine ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Naive Bayes modelini oluştur ve eğit
model = GaussianNB()
model.fit(X_train, y_train)

# 5. Model performansını yazdır
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model doğruluğu: %{accuracy * 100:.2f}")
print(classification_report(y_test, y_pred))

# 6. Yeni müşteri bilgisi al
def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Geçersiz giriş! Lütfen sayısal bir değer girin.")

while True:
    yas = input_int("Yaş (18-65): ")
    if 18 <= yas <= 65:
        break
    print("Yaş 18 ile 65 arasında olmalı.")

while True:
    cinsiyet = input_int("Cinsiyet (1=Erkek, 0=Kadın): ")
    if cinsiyet in [0, 1]:
        break
    print("Cinsiyet sadece 0 veya 1 olabilir.")

while True:
    hizmet = input_int("Hizmet Kalitesi (1-10): ")
    if 1 <= hizmet <= 10:
        break
    print("1 ile 10 arasında bir değer girin.")

while True:
    bekleme = input_int("Bekleme Süresi (1-10): ")
    if 1 <= bekleme <= 10:
        break
    print("1 ile 10 arasında bir değer girin.")

while True:
    temizlik = input_int("Temizlik (1-10): ")
    if 1 <= temizlik <= 10:
        break
    print("1 ile 10 arasında bir değer girin.")

while True:
    menu = input_int("Menü Çeşitliliği (1-10): ")
    if 1 <= menu <= 10:
        break
    print("1 ile 10 arasında bir değer girin.")

while True:
    lezzet = input_int("Lezzet Kalitesi (1-10): ")
    if 1 <= lezzet <= 10:
        break
    print("1 ile 10 arasında bir değer girin.")

while True:
    fiyat = input_int("Fiyat (1-10): ")
    if 1 <= fiyat <= 10:
        break
    print("1 ile 10 arasında bir değer girin.")

# 7. Tahmin yap
new_data = pd.DataFrame([[yas, cinsiyet, hizmet, bekleme, temizlik, menu, lezzet, fiyat]],
                        columns=['Yaş', 'Cinsiyet', 'Hizmet Kalitesi', 'Bekleme Süresi',
                                 'Temizlik', 'Menü Çeşitliliği', 'Lezzet Kalitesi', 'Fiyat'])

predicted_class = model.predict(new_data)[0]
predicted_proba = model.predict_proba(new_data)[0]

# 8. Sonucu göster
if predicted_class == 1:
    print(f"\nMüşteri büyük ihtimalle MEMNUN kalacak. (%{predicted_proba[1]*100:.2f} olasılık)")
else:
    print(f"\nMüşteri büyük ihtimalle MEMNUN KALMAYACAK. (%{predicted_proba[0]*100:.2f} olasılık)")
