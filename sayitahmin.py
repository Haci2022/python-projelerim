
       # sayı tahmin oyunu

import random 

random_sayi=random.randint(1,100) # 1 ile 100 arasında rastgele bir tam sayı üret 

kalan_denemeler=5  # 5 kez sayıyı tahmin edebilirsiniz

puan  = 100 # başlangıç sayısı 

deneme_sayisi=0 # deneme sayısı 

print(f" 1 ile 100 arasinda bir sayi tahmin et ")

print(f"senin baslangıc puanin:{puan}")

def new_func():
    tahmin=int(input("senin tahminin:"))
    return tahmin

while (kalan_denemeler>0):

    tahmin = new_func()

    deneme_sayisi+=1

    if(tahmin<1 or tahmin>100):

        print("lutfen bir ve 100 arasinda bir sayi sec ")
        continue

    if(tahmin==random_sayi):

        print(f"tebrikler sen dogru bir sekilde tahmin ettin!{deneme_sayisi}.deneme")

        print(f"senin toplam puanin:{puan}")

        break

    elif(tahmin<random_sayi):

        print("daha nuyuk bir sayi giriniz!")

    else:


        print("lutfen daha kucuk bir sayi giriniz!")

        deneme_sayisi-=1

        puan-=20

        if(deneme_sayisi>0):

            print(f"kalan deneme sayisi: {deneme_sayisi}")

            print(f"mevcut puan:{puan}")

        else:

            print("maalesef! deneme sayisini astınız daha sonra deneyiniz!")

            print(f"senin toplam puanin:{puan}")



      


                  
