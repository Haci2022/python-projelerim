import random 

sayi = random.randint(10,102)  # bu kod parçacığı 10 ve 102 arasında rastgele sayi üretir

print(sayi)


#shuffle(liste)=> verilen listenin öğelerinin yerini değiştirir.

isimler=["Haci","Serhat","Mazlum","Medet","Yusuf","Bahar"]

print("Kariştirilmadan önce",isimler)


print("\n isimler karıştırılıyor...")

random.shuffle(isimler)

print("karıştırıldıktan sonra",isimler)