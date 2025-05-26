from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np

app = Flask(__name__)

# Eğitilmiş modeli yükle
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Tüm form sonuçlarını tutmak için liste (veritabanı yerine)
veri_kayitlari = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tahmin", methods=["POST"])
def tahmin_et():
    try:
        masa_no = int(request.form['masa_no'])
        yas = int(request.form["yas"])
        cinsiyet = int(request.form["cinsiyet"])
        hizmet = int(request.form["hizmet"])
        bekleme = int(request.form["bekleme"])
        temizlik = int(request.form["temizlik"])
        menu = int(request.form["menu"])
        lezzet = int(request.form["lezzet"])
        fiyat = int(request.form["fiyat"])

        # Veriyi modele uygun hale getir
        girdi = np.array([[yas, cinsiyet, hizmet, bekleme, temizlik, menu, lezzet, fiyat]])
        tahmin = model.predict(girdi)[0]
        tahmin_sonucu = "MEMNUN" if tahmin == 1 else "MEMNUN DEĞİL"

        # En memnun olunan ve en az memnun olunan alanları bul
        puanlar = {
            "Hizmet Kalitesi": hizmet,
            "Bekleme Süresi": bekleme,
            "Temizlik": temizlik,
            "Menü Çeşitliliği": menu,
            "Lezzet Kalitesi": lezzet,
            "Fiyat": fiyat
        }

        en_memnun = max(puanlar, key=puanlar.get)
        en_memnun_degil = min(puanlar, key=puanlar.get)

        # Veriyi kaydet
        veri_kayitlari.append({
            "Masa No": masa_no,
            "Yaş": yas,
            "Cinsiyet": cinsiyet,
            "Hizmet Kalitesi": hizmet,
            "Bekleme Süresi": bekleme,
            "Temizlik": temizlik,
            "Menü Çeşitliliği": menu,
            "Lezzet Kalitesi": lezzet,
            "Fiyat": fiyat,
            "Tahmin": tahmin_sonucu,
            "En Memnun Alan": en_memnun,
            "En Az Memnun Alan": en_memnun_degil
        })

        return redirect("/tesekkur")

    except:
        return redirect("/")

@app.route("/tesekkur")
def tesekkur():
    return render_template("tesekkur.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        kullanici = request.form["kullanici"]
        sifre = request.form["sifre"]

        if kullanici == "sevim" and sifre == "4141":
            return redirect("/panel")
        elif kullanici == "semanur" and sifre == "5361":
            return redirect("/panel")
        elif kullanici == "buse" and sifre == "3535":
            return redirect("/panel")
        elif kullanici == "neslihan" and sifre == "4345":
            return redirect("/panel")

        else:
            return render_template("login.html", hata="❌ Geçersiz kullanıcı adı veya şifre.")
    return render_template("login.html")

@app.route("/panel")
def panel():
    return render_template("panel.html", veriler=veri_kayitlari)

@app.route("/cikis")
def cikis():
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
