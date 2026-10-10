import tkinter as tk

def göster():
    #seçili indeksleri alma 
    seçili_indexler=listbox.curselection()
    if seçili_indexler:
        seçili_diller=[listbox.get(i) for i in seçili_indexler]
        sonuc_label.config(text="Seçilen Diller: " + ", ".join(seçili_diller))
def fonksiyon1():
   print("Buton 0 çalişti")
   sonuc_label.config(text="Buton 0 çalişti")
   yeni_pencere = tk.Toplevel(pencere)
   yeni_pencere.title("Yabanci Dil Seçimi")
   yeni_pencere.geometry("300x250")
  
   baslik = tk.Label(yeni_pencere, text="Yabanci Dil Seçimi", font=("Arial", 14, "bold"))
   baslik.pack(pady=10)
  
      # Seçenekler için kontrol değişkenleri
   ingilizce_var = tk.BooleanVar()
   almanca_var = tk.BooleanVar()
   ispanyolca_var = tk.BooleanVar()
  
   cb1 = tk.Checkbutton(yeni_pencere, text="İngilizce", variable=ingilizce_var)
   cb2 = tk.Checkbutton(yeni_pencere, text="Almanca", variable=almanca_var)
   cb3 = tk.Checkbutton(yeni_pencere, text="İspanyolca", variable=ispanyolca_var)
  
   cb1.pack()
   cb2.pack()
   cb3.pack()
   def onayla_ve_kapat():
          global metin
          secilen_diller = []
          if ingilizce_var.get(): secilen_diller.append("İngilizce")
          if almanca_var.get(): secilen_diller.append("Almanca")
          if ispanyolca_var.get(): secilen_diller.append("İspanyolca")
          
          sonuc = ", ".join(secilen_diller) if secilen_diller else "Dil seçilmedi"
          metin = sonuc
          sonuc_label.config(text=f"Seçilen yabanci diller: {sonuc}")
          print("Kullanicinin seçtiği diller", sonuc)
          yeni_pencere.destroy()
  
   onay_buton = tk.Button(yeni_pencere, text="Seçimi Onayla", command=onayla_ve_kapat)
   onay_buton.pack(pady=20)

def fonksiyon2():
    print("Button 2 tiklandi")
    sonuc_label.config(text="Button 2 tiklandi")
    global metin 
    
    if not metin or metin =="Lütfen önce yabanci di seçiniz!":
        sonuc_label.config(text="Lütfen önce yabanci dil seçiniz!")
        return
    
    hocalar={
        "ingilizce":["Ali hoca", "Mr. Smith", "Zeynep hoca"],
        "almanca":["Özkan hoca", "Herr Schmitt"],
        "ispanyolca":["Ayşegül hoca", "Vanessa hoca"]
    }
    yeni=tk.Toplevel(pencere)
    yeni.title("Hoca Seçimi")
    yeni.geometry("300x250")
    yeni_label=tk.Label(yeni, text="Hoca Seçimi", font=("Arial", 14, "bold"))
    yeni_label.pack(pady=10)
    
    seçilen_hocalar={}
    
    for dil in metin.split(","):
        tk.Label(yeni, text=f"{dil} öğretmenleri: ").pack()
        
        
    var=tk.StringVar()
    var.set("hocalar[dil][0]") #varsayılan olarak ilk hoca seççilir
    
    for hoca in hocalar[dil]:
        rb = tk.Radiobutton(yeni, text=hoca, variable=var, value=hoca)  
        rb.pack()
        
        seçilen_hocalar[dil]=var
        
def onayla_ve_kapat():
     secimler = []
     for dil in "seçilen_hocalar":
       secilen_hoca = "seçilen_hocalar"[dil].get()
       secimler.append(dil + ": " + secilen_hoca)
            
     sonuc_yazisi = "Seçilen hocalar:\n" + "\n".join(secimler)
     sonuc_label.config(text=sonuc_yazisi)
     print("Seçilen hocalar:", secimler)
     "yeni".destroy()
    
     btn_onayla = tk.Button("yeni", text="Onayla", command=onayla_ve_kapat)
     btn_onayla.pack(pady=20)

 
        
    
    
def fonksiyon3():
    print("Button 3 tiklandi")
    sonuc_label.config(text="Button 3 tiklandi")
 
def fonksiyon4():
    print("Button 4 tiklandi")
    sonuc_label.config(text="Button 4 tiklandi")
    
    yeni_pencere=tk.Toplevel(pencere,)
    yeni_pencere.title("Yeni Pencere")
    yeni_pencere.geometry("300x200")
    label=tk.Label(yeni_pencere, text="Ben Yeni Bir Penceredeyim!!!")
    label.pack()
    
    yeni_pencere.grab_set() # o pencereye odaklanma sağlar, diğer pencerelerle etkileşimi engeller 
    yeni_pencere.transient(pencere) # ana pencerenin üstünde açılmasını sağlar
    yeni_pencere.wait_window() # yeni pencere kapanana kadar ana pencerenin etkileşimini engeller
    
 
pencere=tk.Tk()
pencere.title("Listbox Kullanimi")
pencere.geometry("700x400")

metin="" #global değişken, olarak seçilen dilleri saklmak için kullanılır 

#ana pencerenin grid yapılandırması 
pencere.columnconfigure(0, weight=3) #sol sütun, listbox
pencere.rowconfigure(0, weight=3)    #sağ sütun(frame)
pencere.rowconfigure(1, weight=1)
pencere.rowconfigure(2, weight=1)

listbox=tk.Listbox(pencere, selectmode=tk.MULTIPLE)
listbox.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

#listbox a öğe ekleme kısmı 
diller=["python","java","css","go","ruby","c++","c","assembly"]

for dil in diller:
    listbox.insert(tk.END,dil)
    
goster_buton=tk.Button(pencere, text="Seçilenleri göster", command=göster)
goster_buton.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

sonuc_label=tk.Label(pencere, text="",bg="lightgray", width=40, height=2)
sonuc_label.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

#farame oluşturma kısmı
frame=tk.Frame(pencere, bg="lightblue")
frame.grid(row=0 ,column=1, padx=10,pady=5, sticky="nsew")

for i in range(4):
     frame.rowconfigure(i, weight=1)
frame.columnconfigure(0,weight=1)

fonksiyonlar=[fonksiyon1, fonksiyon2, fonksiyon3, fonksiyon4]

for i in range(4):
    btn=tk.Button(frame, text=f"Button {i+1}", command=fonksiyonlar[i])
    btn.grid(row=i, column=0, padx=10, pady=5, sticky="nsew")
    
  # button 1 için bir fonksiyon oluşturma ve yeni pencere açma kısmı 
yabanci_diller=["İngilizce","Almanca","Fransizca","İspanyolca","Japonca","Çince"]
for i, dil in enumerate(yabanci_diller):
    btn=tk.Button(frame, text=dil, command=lambda d=dil: sonuc_label.config(text=f"{d} seçildi"))
    btn.grid(row=i, column=1, padx=10, pady=5, sticky="nsew")
    
pencere.mainloop()