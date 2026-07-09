class Hayvan:
    
    def __init__(self, isim, yas):
        
        self.isim=isim
        self.yas=yas
        
    def ses_cikar(self):
        print("hayvan ses cikariyor!")
        
        
    def kos(self):
        print(f"{self.isim}, hayvan kosuyor.")
        
class Kedi(Hayvan):
    
    def ses_cikar(self):
        
        print(f"{self.isim}, miyavv miyavv")
        
    def tirman(self):
        
        print(f"{self.isim}, tirmaniyor.")
        
    def kos(self):
        
        print(f"{self.isim},kosuyor.")
        
class Kopek(Hayvan):
    
    def ses_cikar(self):
        print(f"{self.isim}, havvv havv havv")
        
    def koru(self):
        print(f"{self.isim}, evi koruyor ")
        
        
    def kos(self):
        print(f"{self.isim}, kosuyor")
        
kedi1 = Kedi("pamuk",3)
kopek1 = Kopek("kuki",5)

kedi1.ses_cikar()
kopek1.ses_cikar()

kedi1.kos()
kedi1.tirman()
kopek1.koru()
kopek1.kos()

        
   