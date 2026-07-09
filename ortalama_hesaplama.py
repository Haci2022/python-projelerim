
"""
print("MERHABA ORTALAMA HESAPLAMAYA HOŞGELDİNİZ!")


sinav1=int(input("Lütfen ilk sınav notunuzu giriniz: "))
sinav2=int(input("Lütfen ikinci sınav notunuzu giriniz: "))
sinav3=int(input("Lütfen üçüncü sınav notunuzu giriniz: "))

ortalama_hesaplama=(sinav1+sinav2+sinav3)/3


sonuc=ortalama_hesaplama

print("sonuc: ",sonuc)
"""

import  random 

random.randint(100,100000)

sayi=random.randint(100,100000)

print(f"{sayi} bu sayı uğurlu sayınız olarak belirlenmiştir.")


markalar=["toyota","BMW","audi","opel","passat","fıat"]

print("\n karıştırılmadan önce",markalar)


print("\n markalar karıştırılıyor...")


random.shuffle(markalar)

print("karıştırıldıktan sonra",markalar)

