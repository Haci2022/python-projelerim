"""
uygulama 2: klavyeden girilen km bilgisini mil cinsinden hesaplayınız.
mil = km/1.609344
"""


mesafeKm =input("kilometreyi giriniz: ")
mesafeMil  = float(mesafeKm)/1.609344
mesafeMil = round(mesafeMil,2)   # bu satır yuvarlama işlemini yapar

print("mesafeKm"+ "km="+ str(mesafeMil)+"mil")