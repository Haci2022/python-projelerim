import random


sıcaklık_değerleri=[]

for i in range(7):
    rastgele_sıcaklık=random.randint(1,35)
    sıcaklık_değerleri.append(rastgele_sıcaklık)

print("Haftanın ortalama sıcaklık değerleri:",sıcaklık_değerleri)

ortalama_sıcaklık=sum(sıcaklık_değerleri) / len(sıcaklık_değerleri)

print("Haftanın sıcaklık değerlerinin ortalaması: ",ortalama_sıcaklık)