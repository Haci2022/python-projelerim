"""
1. kullanıcıdan başlangıç ve bitiş olmak üzere 2 sayi alınız
2.başlangıç ve bitiş arasındaki tek sayiları bulup

a) önce ekrana yazdırınız.
b) daha sonro bunların toplamını bulup ekrana yazdırınız.

"""

baslangic=int(input("Başlangıç değerini giriniz:"))

bitis=int(input("Bitiş değerini giriniz:"))


# tek sayıların tolamı için bir değişken tanımlıyalım
toplam=0

print("Tek sayilar: ")


for sayi in range(baslangic,bitis+1):

    if sayi % 2 !=0: # sayı te sayi ise

        print(sayi)

        toplam+=sayi

print("Tek sayiların toplamı: ",toplam)
    

