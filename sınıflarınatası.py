class insan:
    def __init__(self,isim,yas):
        self.isim=isim
        self.yas=yas
        
        
    def __str__(self):
        
        return f"benim adim {self.isim}, benim yasim{self.yas}"
    
    def __eq__(self, diger):
        
        return(self.isim==diger.isim) and (self.yas==diger.yas)
    
class kare:
    def __init__(self,kenar):
        self.kenar=kenar
    
    def __eq__(self, diger):
        return self.kenar == diger.kenar
    
    def __str__(self,kenar):
        
        return f"kenar uzunlugu:{self.kenar}"
    
insan1=("ahmet", 30)
insan2=("ayşe",25)
insan3=("ahmet",30)
    
if  insan1==insan3:    #burda normalde __eq__komutu kullanılır arka planda 
        print("ayni insan")
        
else:
        print("ayni insan değil")
        
kare1=kare(7)
kare2=kare(5)


if (kare1==kare2):
    print("Ayni kare")
    
else:
    print("Farkli kare")
