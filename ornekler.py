
title = "python ile programlama dersleri"

"""
# 1- 'title' değişkeni içerisindeki karakter sayısı nedir?

adet = len(title)

print(adet)
"""
"""
# 2- 'title' icerisindeki ' python' kelimesini alınız

print(title[:6])
"""

"""
# 3-'title' degiskeninin ik ve son 5 kelimesini yazdır.


print(title[:6])
print(title[:-8])
"""
"""
# 4-' 'title' degiskenini tersten yazın.

print(title[::-1])
"""

# klavyeden girilen öğrenci bilgisine göre örnek verilen cümleyi yazdırınız. f-string kullanılabilir

# cümle = çınar turan isimli öğrencinin 1. notu 60 2. notu 60 ve not ortalaması 60 olarak hesaplanmıştır.

ad =input("ad:")
soyad =input("soyad: ")
not1 = input("not1: ")
not2 = input("not2: ")


sonuc = f"{ad} {soyad} isimli ogrencinin 1. notu {not1}, 2. notu {not2}  ve not ortalamsi 60 olarak hesaplanmistir"

print(sonuc)