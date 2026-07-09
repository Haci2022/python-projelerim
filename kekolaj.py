
import os

# === EKRAN AYARLARI ===
screen = turtle.Screen()
screen.title("Kekolaj FC - Takım Dizilişi")
screen.setup(width=800, height=600)

# === LOGO ARKA PLAN OLARAK EKLE ===
logo_path = "logo.gif"

if os.path.isfile(logo_path):
    screen.bgpic(logo_path)  # Arka plan olarak ayarla
else:
    print("logo.gif bulunamadı! Lütfen doğru klasöre koy ve ismi kontrol et.")
    screen.bgcolor("black")  # Yedek arka plan rengi

# === TURTLE AYARLARI ===
yazi = turtle.Turtle()
yazi.penup()
yazi.hideturtle()
yazi.color("white")  # Yazı rengi

# === OYUNCU POZİSYONLARI ===
oyuncular = {
    "Kaleci: Ali": (0, -250),
    "Sol Bek: Culha": (-200, -100),
    "Sağ Bek: Haci": (200, -100),
    "Orta Saha: Abdulwahid": (0, 0),
    "Sol Kanat: Ondes": (-200, 100),
    "Sağ Kanat: Abdülkadir Özenç": (200, 100),
    "Forvet (C): Adem Tulgar": (0, 200),
}

# === OYUNCULARI YAZDIR ===
for isim, konum in oyuncular.items():
    yazi.goto(konum)
    yazi.write(isim, align="center", font=("Arial", 12, "bold"))

# === PROGRAMI AÇIK TUT ===
turtle.done()
