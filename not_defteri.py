import os
dosya_yolu=r"C:\Users\Haci\Desktop\python-projelerim\notlar.txt"

def not_ekle():
    yeni_not=input("Yeni Notunuzu Giriniz:\n> ")
    
    with open(dosya_yolu,"a",encoding="utf-8") as dosya:
        dosya.write(yeni_not + "\n")
        print("Notunuz kaydedilidi..")
        
def notlari_goster():
    print("\n-----NOTLARİNİZ-----")
    if os.path.exists(dosya_yolu):
        with open(dosya_yolu,"r",encoding="utf-8") as dosya:
            içerik=dosya.read()
            if içerik.strip()=="":
                print("Henüz not girilmemiş...")
            else:
                print(içerik)
    else:
        print("Henüz hiç not yok!")
        print("----------------\n")
        
def notlari_temizle():
    with open(dosya_yolu,"w",encoding="utf-8") as dosya:
        pass # tüm dosyalar silinir ya da sıfırlanır 
    
    print("Tüm notlar silindi!\n")
    print("şuanda yazili not gözükmüyor!!!")

def menu():
    while True:
        print("======================")
        print("Not defteri uygulamasi")
        print("======================")
        print("1) Not Ekle")
        print("2) Notlari Göster")
        print("3) Notlari Temizle")
        print("4) Çikiş")

        secim = input("Seçiminiz (1-4): ")

        if secim == "1":
            not_ekle()

        elif secim == "2":
            notlari_goster()

        elif secim == "3":
            notlari_temizle()

        elif secim == "4":
            print("Not uygulamasindan çikiş yapiliyor....")
            break

        else:
            print("Hatali seçim! (1-4) arasinda bir seçim yapiniz lütfen!")
menu()