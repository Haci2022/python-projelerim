import tkinter as tk
import random

# =========================================================
# AYARLAR
# =========================================================

GENISLIK = 1200
YUKSEKLIK = 800

YESIL = "#07883F"
KIRMIZI = "#E30613"
SARI = "#FFD700"
BEYAZ = "#FFFFFF"
SIYAH = "#111111"
KOYU_YESIL = "#063B22"

# =========================================================
# PENCERE
# =========================================================

pencere = tk.Tk()
pencere.title("🎉 Osman Abi - Doğum Günü 🎉")
pencere.geometry("1200x800")
pencere.resizable(False, False)

canvas = tk.Canvas(
    pencere,
    width=GENISLIK,
    height=YUKSEKLIK,
    highlightthickness=0
)

canvas.pack()

# =========================================================
# YEŞİL - KIRMIZI ARKA PLAN
# =========================================================

serit = 65

for y in range(0, YUKSEKLIK, serit):

    if (y // serit) % 2 == 0:
        renk = YESIL
    else:
        renk = KIRMIZI

    canvas.create_rectangle(
        0,
        y,
        GENISLIK,
        y + serit,
        fill=renk,
        outline=""
    )

# =========================================================
# KONFETİLER
# =========================================================

konfetiler = []

konfeti_renkleri = [
    "#00FFFF",
    "#FFFF00",
    "#FF00FF",
    "#FFFFFF",
    "#FFA500",
    "#00FF00"
]

for i in range(100):

    x = random.randint(0, GENISLIK)
    y = random.randint(0, YUKSEKLIK)

    boyut = random.randint(5, 10)

    konfeti = canvas.create_oval(
        x,
        y,
        x + boyut,
        y + boyut,
        fill=random.choice(konfeti_renkleri),
        outline=""
    )

    konfetiler.append([
        konfeti,
        x,
        y,
        random.randint(2, 5)
    ])


def konfeti_hareket():

    for k in konfetiler:

        k[2] += k[3]

        if k[2] > YUKSEKLIK:
            k[2] = -10
            k[1] = random.randint(0, GENISLIK)

        canvas.coords(
            k[0],
            k[1],
            k[2],
            k[1] + 8,
            k[2] + 8
        )

    pencere.after(30, konfeti_hareket)


# =========================================================
# BAŞLIK
# =========================================================

canvas.create_text(
    600,
    55,
    text="OSMAN ABİ'NİN",
    fill=BEYAZ,
    font=("Arial", 46, "bold")
)

canvas.create_text(
    600,
    115,
    text="DOĞUM GÜNÜ",
    fill=SARI,
    font=("Arial", 48, "bold")
)

# =========================================================
# AMEDSPOR MODU
# =========================================================

canvas.create_rectangle(
    410,
    175,
    790,
    230,
    fill=SIYAH,
    outline=SARI,
    width=4
)

canvas.create_text(
    600,
    202,
    text="⚽ AMEDSPOR MODU: AKTİF ⚽",
    fill=SARI,
    font=("Arial", 21, "bold")
)

# =========================================================
# KALPLER
# =========================================================

canvas.create_text(
    600,
    260,
    text="♥  ♥  ♥  ♥  ♥  ♥  ♥  ♥",
    fill=BEYAZ,
    font=("Arial", 30, "bold")
)

# =========================================================
# AMEDSPOR TARZI KALKAN
# =========================================================

# Dış kalkan
canvas.create_polygon(
    600, 300,
    680, 335,
    665, 465,
    600, 525,
    535, 465,
    520, 335,
    fill=BEYAZ,
    outline=KIRMIZI,
    width=5
)

# İç kalkan
canvas.create_polygon(
    600, 315,
    665, 345,
    650, 450,
    600, 500,
    550, 450,
    535, 345,
    fill=YESIL,
    outline=BEYAZ,
    width=3
)

canvas.create_text(
    600,
    365,
    text="AMED",
    fill=BEYAZ,
    font=("Arial", 27, "bold")
)

canvas.create_text(
    600,
    405,
    text="SPOR",
    fill=BEYAZ,
    font=("Arial", 27, "bold")
)

canvas.create_text(
    600,
    450,
    text="⚽",
    fill=BEYAZ,
    font=("Arial", 28)
)

# =========================================================
# SOL PANEL
# =========================================================

canvas.create_rectangle(
    35,
    540,
    535,
    735,
    fill=KOYU_YESIL,
    outline=SARI,
    width=4
)

canvas.create_text(
    285,
    565,
    text="🎂 İYİ Kİ DOĞDUN OSMAN ABİ!",
    fill=SARI,
    font=("Arial", 19, "bold")
)

canvas.create_text(
    65,
    605,
    text="Yeni yaşında;",
    anchor="w",
    fill=BEYAZ,
    font=("Arial", 17, "bold")
)

mesajlar = [
    "⚽ Bol Amedspor galibiyeti",
    "😂 Bol kahkaha",
    "☕ Bol çay",
    "🐜 Bol böcek videosu",
    "🎉 Bol mutluluk"
]

y = 635

for mesaj in mesajlar:

    canvas.create_text(
        65,
        y,
        text=mesaj,
        anchor="w",
        fill=BEYAZ,
        font=("Arial", 15, "bold")
    )

    y += 20

# =========================================================
# SAĞ PANEL
# =========================================================

canvas.create_rectangle(
    665,
    540,
    1165,
    735,
    fill=KOYU_YESIL,
    outline=SARI,
    width=4
)

canvas.create_text(
    915,
    565,
    text="💻 BİLGİ İŞLEM",
    fill=SARI,
    font=("Arial", 21, "bold")
)

canvas.create_text(
    915,
    595,
    text="SİSTEM ANALİZİ",
    fill=SARI,
    font=("Arial", 21, "bold")
)

analizler = [
    ("Komiklik", "%100", "#00FF00"),
    ("Amedspor sevgisi", "%1000", "#00FF00"),
    ("Böcek sevgisi", "SINIRSIZ", "#00FF00"),
    ("Çay seviyesi", "KRİTİK", "#FF3333")
]

y = 630

for isim, deger, renk in analizler:

    canvas.create_text(
        700,
        y,
        text=isim,
        anchor="w",
        fill=BEYAZ,
        font=("Arial", 16, "bold")
    )

    canvas.create_text(
        1125,
        y,
        text=deger,
        anchor="e",
        fill=renk,
        font=("Arial", 16, "bold")
    )

    y += 24

# =========================================================
# ALT YAZI
# =========================================================

canvas.create_text(
    600,
    755,
    text="♥ NICE MUTLU YILLARA OSMAN ABİ! ♥",
    fill=SARI,
    font=("Arial", 23, "bold")
)

# =========================================================
# BÖCEKLER
# =========================================================

bocekler = [
    ("🐜", "Makarayız Abi 😂"),
    ("🐞", "İyi ki doğdun Abi! 🎉"),
    ("🪲", "Böcek videosu şart! 😂"),
    ("🦗", "Çay hazır mı Abi? ☕"),
    ("🪳", "Amedspor şampiyon! ⚽")
]

aktif_bocekler = []


class Bocek:

    def __init__(self, emoji, mesaj, baslangic_y):

        self.emoji = emoji
        self.mesaj = mesaj

        self.x = -80
        self.y = baslangic_y

        self.hiz = random.randint(3, 5)

        self.balik = canvas.create_text(
            self.x,
            self.y,
            text=self.emoji,
            font=("Arial", 30)
        )

        self.konusma = None
        self.konusma_yazisi = None
        self.konusuyor = False

        aktif_bocekler.append(self)

    def hareket_et(self):

        self.x += self.hiz

        canvas.coords(
            self.balik,
            self.x,
            self.y
        )

        # Belirli bölgeye gelince konuş
        if (
            100 < self.x < 300
            and not self.konusuyor
        ):

            self.konusuyor = True

            self.konusma = canvas.create_rectangle(
                self.x - 20,
                self.y - 65,
                self.x + 250,
                self.y - 20,
                fill=BEYAZ,
                outline=SIYAH,
                width=2
            )

            self.konusma_yazisi = canvas.create_text(
                self.x + 115,
                self.y - 42,
                text=self.mesaj,
                fill=SIYAH,
                font=("Arial", 12, "bold")
            )

            pencere.after(
                2000,
                self.konusmayi_kapat
            )

        # Ekrandan çıkınca yeniden başlat
        if self.x > GENISLIK + 80:

            self.x = -80
            self.konusuyor = False

        pencere.after(
            35,
            self.hareket_et
        )

    def konusmayi_kapat(self):

        if self.konusma is not None:
            canvas.delete(self.konusma)

        if self.konusma_yazisi is not None:
            canvas.delete(self.konusma_yazisi)

        self.konusma = None
        self.konusma_yazisi = None


# Farklı yüksekliklerde böcekler
Bocek("🐜", "Makarayız Abi 😂", 320).hareket_et()
Bocek("🐞", "İyi ki doğdun Abi! 🎉", 400).hareket_et()
Bocek("🪲", "Böcek videosu şart! 😂", 470).hareket_et()
Bocek("🦗", "Çay hazır mı Abi? ☕", 280).hareket_et()
Bocek("🪳", "Amedspor şampiyon! ⚽", 510).hareket_et()

# =========================================================
# KUTLAMA BUTONU
# =========================================================

def kutla():

    canvas.create_rectangle(
        300,
        685,
        900,
        730,
        fill=KIRMIZI,
        outline=SARI,
        width=3,
        tags="kutlama"
    )

    canvas.create_text(
        600,
        708,
        text="🎉 OSMAN ABİİİ! İYİ Kİ DOĞDUN! 🎉",
        fill=BEYAZ,
        font=("Arial", 17, "bold"),
        tags="kutlama"
    )

    pencere.after(
        3000,
        lambda: canvas.delete("kutlama")
    )


buton = tk.Button(
    pencere,
    text="🎂 DOĞUM GÜNÜNÜ KUTLA 🎂",
    command=kutla,
    font=("Arial", 14, "bold"),
    bg=YESIL,
    fg=BEYAZ,
    activebackground=KIRMIZI,
    activeforeground=BEYAZ,
    relief="raised",
    bd=4,
    cursor="hand2"
)

canvas.create_window(
    600,
    785,
    window=buton
)

# =========================================================
# BAŞLAT
# =========================================================

konfeti_hareket()

pencere.mainloop()