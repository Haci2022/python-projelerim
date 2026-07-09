#  kullanım formatı

#  for geçici_değişken in koleksiyon
     # dögü içerisinde yazılacak kod parçacığı


"""
araba_modelleri=["Toyota","Opel","Nisan","BMW","Audi","Porche"]

for araba in araba_modelleri:

    print(araba)
    print("en sevdiğim araba",araba)


print("\Hoşçakalın...")
"""


"""
sayilar=[12,13,14,115,7,6,16,87,91,22,21,29,20]


for sayi in sayilar:

    print(sayi)

    print("en sevdiğim sayi",sayi)


print("\bye...")
"""

#range()=> range fonksiyonu sayı üretme işine yarar.

# range(stop)range(5)=> 0,1,2,3,4 duracağı sayıya kadar sadece yazar 5 dahil değil yani
# range(start,stop)range(2,5)=> 2,3,4 
# range(start,stop,step)range(2,10,2)=> 2,4,6,8 sondaki step basamak anlamına gelir kaçar kaçar artacağını anlatır 


#for sayi in range(10):

 #   print(sayi)

# range() fonksiyonunu kulanarak otomatik liste oluşturma 

#sayilar=list(range(20))
#print(sayilar)

# 1 den 100 e kadar sayıların toplamını yazınız.

toplam=0

for sayilar in range(1,101):
    print(sayilar)
    toplam=toplam+sayilar

print("\n Toplam: ",toplam)