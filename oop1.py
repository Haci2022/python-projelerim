
#PascalCase=> TeslaOtomobil
class Tesla:
    tesla_count=0  #nesne değişkeni
    sis_farlari=2   #nesne değişkeni
        
    gecerli_renkler=["beyaz","siyah","turuncu"]
    gecerli_bataryalar=["uzun menzili","kisa menzili"]
    gecerli_jantlar=[20,21,22]
    gecerli_otopilot=[True , False]
    #jant=inç cinsinden hesaplanmıştır 
    def __init__(self, renk="Siyah", batarya="Uzun menzili", jant=24, otopilot=True):
        # nesnelerin kontorlü yapılmıştır 
        if renk in Tesla.gecerli_renkler:
            self.__renk=renk  # nesne değişkeni
            
        else:
            self.__renk="Beyaz"
            
        if batarya in Tesla.gecerli_bataryalar:
            self.__batarya=batarya  # nesne değişkeni
            
        else:
            self.__batarya="uzun menzili"
            
        if jant in Tesla.gecerli_jantlar:
            self.__jant=jant
            
        else:
            self.__jant=21
            
        if otopilot in Tesla.gecerli_otopilot:
            self.__otopilot=otopilot
            
        else:
            self.__otopilot=True
            
        if renk in Tesla.gecerli_renkler:
            self.__renk=renk  #nesne değşkeni 
        else:
            self.__renk="Beyaz"
        self.renk = renk
        self.batarya = batarya        # bu yazdığımız renk,otopilot,jant,batarya gibi şeyler hepsi nesnedir 
        self.jant = jant
        self.otopilot = otopilot
        self.hiz=0
        Tesla.tesla_count +=1 #

    def bilgi_goster(self):
        print(f"Renk: {self.renk}, Batarya: {self.batarya}, Jant: {self.jant},"
              f"Otopilot: {self.otopilot},Hiz:{self.hiz}")
    
    #arabayı hızlandırıyoruz
    def hizlan(self,miktar):
        self.hiz +=miktar
    
    #arabayı yavaşlatıyoruz
    def yavasla(self,miktar):
        self.hiz -=miktar
    #araba eksi hızda gidemeyeceği için mecbur if bloğuyla arabayı durduracaz 
        if self.hiz<0:
            self.hiz=0
            
    #get methodu ile hız k0ntrolu
    
    def get_hiz(self):
        return self.__hiz
    print("arabayi çaliştir!")
     #getter methodu batarya
    def get_batarya(self):
        return self.batarya
    
    #setter methodu batarya
    
    def set_batarya(self,yeni_batarya):
        
        if yeni_batarya in Tesla.gecerli_bataryalar:
            
            self.__batarya=yeni_batarya
            
        else:
            print("dikkat! geçersiz batarya secimi")
            
    #getter ile jant methodu
    def get_jant(self):
        return self.jant
    
    #setter methodu ile jantlat 
    def set_jant(self, yeni_jant):
    
       if 19<=yeni_jant>=23:
        self.__jant = yeni_jant
       else:
        print("Dikkat! Geçersiz jant değeri")
    #getter ile otopilot methodu
    def get_otopilot(self):
        return self.otopilot
    # setter ile otopilot methodu
    def set_otopilot(self,yeni_otopilot):
        if isinstance(yeni_otopilot,bool):
            self.__otopilot=yeni_otopilot
        else:
            
            print("Dikkat! gecersiz otopilot değeri")
            
    #gett methodfu ile renkler
    
    def get_renk(self):
        return self.__renk
    
    #sett methodu ile renkler 
    
    def set_renk(self,yeni_renk):
        if yeni_renk in Tesla.gecerli_renkler:
            self.__renk=yeni_renk
        else:
            print("Dikkat! gecersiz renk secimi yapildi")
#kenidimize ait nesneleri oluşturuyoruz
Benim_teslam = Tesla()
Benim_teslam.bilgi_goster()
Benim_teslam.jant = 24
Benim_teslam.hizlan(200)
Benim_teslam.hizlan(10)
Benim_teslam.yavasla(80)
Benim_teslam.bilgi_goster()

ademin_teslasi = Tesla("siyah", "kisa menzili", 20, False)
ademin_teslasi.hizlan(70)
ademin_teslasi.hizlan(30)
ademin_teslasi.yavasla(10)
ademin_teslasi.bilgi_goster()

sametin_teslasi = Tesla("gri", "uzun menzili", 24, True)
sametin_teslasi.hizlan(200)
sametin_teslasi.hizlan(25)
sametin_teslasi.yavasla(85)
sametin_teslasi.bilgi_goster()

malinin_teslasi = Tesla("siyah", "kisa menzili", 22, False)
malinin_teslasi.hizlan(40)
malinin_teslasi.hizlan(110)
malinin_teslasi.yavasla(20)
malinin_teslasi.bilgi_goster()





            