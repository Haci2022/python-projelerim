"""
uygulama 1: yari çapi verilen bir dairenin alan ve çevresini hesaplayınız.
alan = pi*r*r
cevre = 2*pi*r


#uygulama 2: klavyeden girilen km bilgisini mil cinsinden hesaplayınız.
mil = km/1.609344
"""


#pi  = 3.14

#r = float(input("yaricapi giriniz: "))

#alan = pi* (r**2)
#cevre = 2*pi*r

#print("alan: "+str(alan))
#print("cevre: "+str(alan))

mesafeKM = input("km: ")
mesafeMil = float ("mesafeMil")/1609344
mesafeMil = round(mesafeMil,2)     # bu satır çıkan sonucu yuvarlar

print("mesafeKm "+ "km="+ str(mesafeMil)+"mil")