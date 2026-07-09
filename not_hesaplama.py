import math

sinav1=int(input("lutfen 1. sinavin notunu giriniz: "))

sinav2=float(input("lutfen 2. sinavin notunu giriniz: "))

sinav3=int(input("lutfen 3. sinavin notunu giriniz: "))

ortalama=(sinav1+sinav2+sinav3)/3

# yuvarlanmış ortalama 
yuvarlanmis_ortalama= round(ortalama,1)


print(f" ortalama {yuvarlanmis_ortalama}")