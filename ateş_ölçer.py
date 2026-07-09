# kullanıcıdan vücud sıcaklığını alınız (float)

sicaklik=float(input("lütfen vücud sıcaklık değerini giriniz: "))


# ateş seviyesini kontrol et ve ilgili mesajı yaz

if sicaklik>37:

    print("dikkat! yüksek ateş...")
    print("en yakın sürede doktorunuza görünün!")


else:
    print("normal ateş!")
    print("endişelenecek bir durum yok!")

print("Hoşçakalın...")