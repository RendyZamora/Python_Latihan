from flask import Flask, render_template, request
from datetime import datetime
from groq import Groq 
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

AI_KEY = ""

client = Groq(api_key = AI_KEY)

def scrape():
    url= "https://news.detik.com"
    response = requests.get(url)
    element =  BeautifulSoup(response.content, "html.parser")
    
    headlines = []
    for h in element.find_all("a", class_="media__link", limit=10):
        text = h.get_text(strip=True)
        if text:  # hanya masukkan kalau ada isi
            headlines.append(text)

    return headlines

def ai_call(year):
    try:
        chat_completion = client.chat.completions.create(
            messages = [
                {
                    "role" : "user",
                    "content" : f"berikan satu fakta menarik seputar teknologi yang terjadi pada tahun {year}"
                }
            ],
            model="llama-3.1-8b-instant",
            stream= False
        )

        ai_output = chat_completion.choices[0].message.content

        return ai_output
    except Exception:
        return "Maaf, AI saat ini tidak bisa digunakan"


@app.route("/")
def home():
    scraping = scrape()
    nama = "Rendy Zamora"
    halaman = "Home"

    return render_template("home.html", berita = scraping)

@app.route("/about", methods =['GET','POST'])
def about():
    if request.method == 'POST' :
        tahunLahir = int(request.form['usia'])
        nama = request.form['nama']
        tahunIni = datetime.now().year
        usia_sekarang = tahunIni - tahunLahir

        ai_hasil = ai_call(tahunLahir)

        print(ai_hasil)
        return render_template("about.html", usia = usia_sekarang, nama = nama, ai_hasil = ai_hasil)

    return render_template("about.html", usia = None)

if __name__ == "__main__":
    app.run(debug=True)

