#grid yerleşim

import tkinter as tk 
from tkinter import messagebox

def giris_yap():
    ad=entry_ad.get()
    soyad=entry_soyad.get()
    mesaj=f"Merhaba {ad} {soyad}"
    #mesajı yazdıracazğız 
    print(mesaj)
    
   #küçük mesaj penceresi açacaz
    messagebox.showinfo("Karşilama", mesaj )
    
root=tk.Tk()
root.title("Grid kullanimi")
root.geometry("300x200")
#sütunların genişleyebilmesi sağlıyoruz
root.columnconfigure(0, weight=1)
root.columnconfigure(1,weight=3)
# etiketler 
label_ad=tk.Label(root,  text="Adiniz",bg="blue",fg="white")
label_soyad=tk.Label(root, text="Soyadiniz",bg="blue",fg="white")
label_yaş=tk.Label(root, text="Yaşiniz",bg="blue",fg="white")

#metin giriş kutuları 
entry_ad=tk.Entry(root)
entry_soyad=tk.Entry(root)
entry_yaş=tk.Entry(root)

#buton oluşturalım
buton_giriş=tk.Button(root, text="Giriş yap", command=giris_yap,  bg="black", fg="white")

# grid yerleşimi ile bileşenleri birleştiriyoruz 
label_ad.grid(row=0,column=0,padx=10,pady=5)
label_soyad.grid(row=1,column=0,padx=10,pady=5)
label_yaş.grid(row=2,column=0,padx=10,pady=5)
#metin girişleri
entry_ad.grid(row=0,column=1,padx=10,pady=5)
entry_soyad.grid(row=1,column=1,padx=10,pady=5)
entry_yaş.grid(row=2,column=1,padx=10,pady=5)

#buttonları oluşturalım 
buton_giriş.grid(row=3,column=0,columnspan=2,pady=5, sticky="nsew")

root.mainloop()