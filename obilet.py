import tkinter as tk
from tkinter import ttk, messagebox

# Pencere
pencere = tk.Tk()
pencere.title("Otobüs Bileti Satın Alma")
pencere.geometry("400x500")
pencere.resizable(False, False)

# Başlık
tk.Label(pencere, text="Otobüs Bileti Satın Al",
         font=("Arial", 14, "bold")).pack(pady=10)

# Ad Soyad
tk.Label(pencere, text="Ad Soyad").pack()
ad_entry = tk.Entry(pencere)
ad_entry.pack()

# Mail
tk.Label(pencere, text="E-posta").pack()
mail_entry = tk.Entry(pencere)
mail_entry.pack()

# Telefon
tk.Label(pencere, text="Telefon").pack()
tel_entry = tk.Entry(pencere)
tel_entry.pack()

# Otobüs Firması
tk.Label(pencere, text="Otobüs Firması").pack()
firma = ttk.Combobox(pencere, values=[
    "Kamil Koç", "Metro Turizm", "Pamukkale", "Lüks Amed"
])
firma.pack()

# Nereden
tk.Label(pencere, text="Nereden").pack()
nereden = ttk.Combobox(pencere, values=[
    "Diyarbakır", "Ankara", "İstanbul", "İzmir"
])
nereden.pack()

# Nereye
tk.Label(pencere, text="Nereye").pack()
nereye = ttk.Combobox(pencere, values=[
    "Diyarbakır", "Ankara", "İstanbul", "İzmir"
])
nereye.pack()

# Tarih
tk.Label(pencere, text="Tarih (GG/AA/YYYY)").pack()
tarih_entry = tk.Entry(pencere)
tarih_entry.pack()

# Fiyat Label
fiyat_label = tk.Label(pencere, text="Bilet Fiyatı: -- TL",
                       font=("Arial", 11, "bold"))
fiyat_label.pack(pady=10)

# Fiyat Hesaplama
def fiyat_hesapla():
    if nereden.get() != "" and nereye.get() != "":
        if nereden.get() == nereye.get():
            fiyat = 100
        else:
            fiyat = 350
        fiyat_label.config(text=f"Bilet Fiyatı: {fiyat} TL")
        return fiyat
    return 0

def secim_degisti(event):
    fiyat_hesapla()

nereden.bind("<<ComboboxSelected>>", secim_degisti)
nereye.bind("<<ComboboxSelected>>", secim_degisti)

# Bilet Al
def bilet_al():
    fiyat = fiyat_hesapla()

    if (ad_entry.get() == "" or mail_entry.get() == "" or
        tel_entry.get() == "" or firma.get() == "" or
        nereden.get() == "" or nereye.get() == "" or
        tarih_entry.get() == ""):
        messagebox.showerror("Hata", "Tüm alanları doldurun!")
    else:
        messagebox.showinfo(
            "Bilet Alındı",
            f"Ad: {ad_entry.get()}\n"
            f"Mail: {mail_entry.get()}\n"
            f"Telefon: {tel_entry.get()}\n"
            f"Firma: {firma.get()}\n"
            f"Güzergah: {nereden.get()} → {nereye.get()}\n"
            f"Tarih: {tarih_entry.get()}\n"
            f"Fiyat: {fiyat} TL\n\n"
            "Biletiniz başarıyla oluşturuldu ✅"
        )

# Button
tk.Button(pencere, text="Bilet Al",
          bg="green", fg="white",
          width=25, height=2,
          command=bilet_al).pack(pady=15)

# Çalıştır
pencere.mainloop()

