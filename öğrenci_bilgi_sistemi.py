# bu kod bir okulun öğrenci ekle,sil,göster gibi parametrelerini uygulayıp kullanıcıların işini daha da kolay hale getirir

import ogrenciler


class ogrenci:
    def __init__(self,numara,ad,soyad,ortalama=None):
        self.numara=numara
        self.ad=ad
        self.soyad=soyad
        self.ortalama=ortalama
    def notu_gir(self,ortalama):
        if 0 <= ortalama <= 100:
            self.ortalama=ortalama
        else:
            print("geçersiz not girdiniz 1 ile 100 arasinda bir değer giriniz!")
            
    def bilgi_goster(self):
        sonuc=(
            f"{self.numara} - {self.ad} - {self.soyad}, "
            f"ortalama: {self.ortalama if self.ortalama is not None else 'Henüz not  girilmedi!'}"
                 
        )
        return sonuc
    
    def menu_goster():
        print("""
              
                 ___  _  ___   _ _       ____ _[] _     ____ _[]   ____ _[] ____ _____ _____ __  __ _[] 
  / _ \| |/ / | | | |     | __ )_ _| |   / ___|_ _| / ___|_ _/ ___|_   _| ____|  \/  |_ _|
 | | | | ' /| | | | |     |  _ \| || |  | |  _ | |  \___ \| |\___ \ | | |  _| | |\/| || | 
 | |_| | . \| |_| | |___  | |_) | || |__| |_| || |   ___) | | ___) || | | |___| |  | || | 
  \___/|_|\_\\___/|_____| |____/___|_____\____|___| |____/___|____/ |_| |_____|_|  |_|___|
                                                                                            
              """)
        print("=======================")
        print("\nöğrenci bilgi sistemi")
        print("=======================")
        print("1-öğrenci ekle")
        print("2-öğrenci sil")
        print("3-öğrenci listele")
        print("4-öğrenci not gir")
        print("5-öğrenci bilgilerini göster")
        print("6-okuldaki tüm öğrencilerin not ortalamasini hesapla")
        print("7-çikiş")
        
    def okul_ortalama_hesapla(ogrenciler):
        if len(ogrenciler) == 0:
            print("henüz not girilmediği için ortalama hesaplanamaz!")
            return
        
        toplam=0
        not_girilen_ogrenci_sayisi=0
        
        for ogrenci in ogrenciler.values():
            if ogrenci.ortalama is not None:
                toplam=ogrenci.ortalama
                not_girilen_ogrenci_sayisi +=1
            if not_girilen_ogrenci_sayisi > 0:
                okul_ortalamasi = toplam / not_girilen_ogrenci_sayisi
            else:
                okul_ortalamasi = 0
                print(f"okulun gtenel ortalamasi {okul_ortalamasi}")
    def main():
        öğrenciler = {}

    while True:
        menu_goster()
        secim = input("Lütfen seçiminizi yapiniz: ")
        
        if secim == "1":
            numara=input("öğrenci numarasini giriniz: ")
            ad=input("öğrencinin adini giriniz: ")
            soyad=input("öğrencinin soyadini giriniz: ")
            if numara in ogrenciler:
                print("bu öğrenci no zaten mevcut!")
            else:
                ogrenciler[numara]= ogrenciler(numara,ad,soyad)
                print(f"{ad} {soyad} eklendi.")
        elif secim == "2":
                numara=input("silinecek numarayi griniz: ")
                if numara in  ogrenciler:
                    del ogrenciler [numara]
                    
                    print(f" öğrenci {numara} silindi.")
                else:
                    print("öğrenci bulunamadi!")
                
        elif secim == "3":
            if len(ogrenciler) > 0:
                print("\n Öğrenci Listesi.")
                for ogrenci in ogrenciler.values:
                    print(ogrenci.bilgi_goster())
                    
            else:
                print("Henüz öğrenci eklenmemiş!")
                
        elif secim == "4":
            numara=input("notu girilecek öğrenci numarasi")
            if numara in ogrenciler:
                try:
                    ortalama=float(input("ortalama not giriniz (1-100)"))
                    ogrenciler[numara].not_gir(ortalama)
                    print("Not başariyla eklendi!")
                    
                except ValueError:
                    print("Geçersiz not! lütfen sayi griniz.")  
            else:
                print("öğrenci bulunamadi!")       
                
        elif secim == "5":
            numara=input("bilgilierini görmek istediğiniz öğrencinin no:  ")
            if numara in ogrenciler:
             print(ogrenciler[numara].bilgi_goster())
            else:
                print("öğrenci bulunamadi!")
                
        elif secim == "6":
            okul_ortalama_hesapla(ogrenciler)
            
        elif secim == "7":
            print("çikiş yapiliyor...")
            break
        
        else:
            print("Lütfen 1 ve 7 arasinda bir sayi seçin!")
                       
                    
                                              
            
            
          
        
            
        