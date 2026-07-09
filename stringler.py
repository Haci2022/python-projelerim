metin=input("Lütfen bir metin giriniz: ")

print(metin.upper()) # cümleyi büyük harflere dönüştürür
print(metin)

print(" ".join(metin.split()[::-1]))  # metni terseten yazar yani: güzel. çok hava bugün merhaba join birleştirme işlemini yapar. Split ise ayırma işlemini yapar
print(metin)

print(metin.lower()) # cümleyi küçük harflere çevirir
print(metin)

print(metin.title()) # cümlenin ilk harfini tek büyük yazar
print(metin)

print(metin.capitalize()) # cümledeki ilk harfleri büyük yazar
print(metin)

