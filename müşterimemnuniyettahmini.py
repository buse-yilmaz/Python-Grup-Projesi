import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


df = pd.read_csv("Python_Veriler_400_ortalamasiz.csv")


X = df[['Yaş', 'Cinsiyet', 'Hizmet Kalitesi', 'Bekleme Süresi', 'Temizlik',
        'Menü Çeşitliliği', 'Lezzet Kalitesi', 'Fiyat']]
y = df['Memnuniyet']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = GaussianNB()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model doğruluğu: %{accuracy * 100:.2f}")


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


new_data = pd.DataFrame([[yas, cinsiyet, hizmet, bekleme, temizlik, menu, lezzet, fiyat]],
                        columns=['Yaş', 'Cinsiyet', 'Hizmet Kalitesi', 'Bekleme Süresi',
                                 'Temizlik', 'Menü Çeşitliliği', 'Lezzet Kalitesi', 'Fiyat'])

predicted_class = model.predict(new_data)[0]

alanlar = ['Hizmet Kalitesi', 'Bekleme Süresi', 'Temizlik',
           'Menü Çeşitliliği', 'Lezzet Kalitesi', 'Fiyat']

puanlar = [hizmet, bekleme, temizlik, menu, lezzet, fiyat]
alan_puan = dict(zip(alanlar, puanlar))

en_memnun_alan = max(alan_puan, key=alan_puan.get)
en_memnun_puan = alan_puan[en_memnun_alan]

en_memnun_deg_alan = min(alan_puan, key=alan_puan.get)
en_memnun_deg_puan = alan_puan[en_memnun_deg_alan]


if predicted_class == 1:
    print(f"\nMüşteri Memnun")
else:
    print(f"\nMüşteri Memnun Değil")

print(f"En memnun kalınan alan: {en_memnun_alan} ({en_memnun_puan}/10)")
print(f"En memnun kalmadığı alan: {en_memnun_deg_alan} ({en_memnun_deg_puan}/10)")





