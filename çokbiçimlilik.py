
class Kus:
    def ses_cikar(self):
     print("cik cik cik")

def hayvan_konustur(hayvan):
 hayvan.ses_cikar()

kus1 = Kus()
hayvan_konustur(kus1)


class kedi:
    
    def ses_cikar(self):
        print("miyavv miyavv miyavv")
        
    def hayvan_konustur(hayvan):
        hayvan.ses_cikar()
kedi1=kedi()
hayvan_konustur(kedi1)


class Araba:
    def harekete_gec(self):
        print("Araba hareket etmeye başladi")

class ElektrikliAraba:
    def harekete_gec(self):
        print("Elektrikli araba yavaşça yola çikiyor")

class Kamyon:
    def harekete_gec(self):
        print("Kamyon ağir ağir hareket ediyor")

def sur(arac):
    arac.harekete_gec()

araba = Araba()
elektrikli_araba = ElektrikliAraba()
kamyon = Kamyon()

sur(araba)
sur(elektrikli_araba)
sur(kamyon)