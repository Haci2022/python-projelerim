#string metotlarına giriş capitalize

#text = "merhaba phton!"


#sonuc = text.capitalize()


#print(sonuc)


# string metotlarına giriş casefold kullanıldı. casefold ve lower aynıdır sadece casefold lowerden daha güçlüdür

#text = "merhaba phyton!!"


#sonuc = text.casefold()

#print(sonuc)


#stringlere giriş title kullanımı her kelimenin ilk harfini büyük yazar


#text = "merhaba phyton!"


#sonuc =text.title()

#print(sonuc)


#stringlere giriş swapcase kullanımı değişşim anlamına gelir büyükse küçük yazar. Kçükse büyük yazar

#text = "merhaba phyton!"

#sonuc = text.swapcase()

#print(sonuc)


#stringlere giriş islower kullanımı bütün kelimeler küçükse değeri true döndürür

#text = "merhaba dünya!"


#sonuc = text.islower()

#print(sonuc)


#stringlere giriş isupper kullanımı kelimelerin hepsi büyük yazılmışsa değer true döner

#text = "MERHABA DÜNYA"

#sonuc = text.isupper()

#print(sonuc)

#stringleri ortalamak için kullannılan komuttur
#text = "merhaba dunya!"

#print("1. title()- her kelimenin ilk harfi buyuk ")

#metin = "phyton string metotları"

#print(metin.title())

#print()


#print("2. strip()- bas ve sondaki boslukları siler ")

#metin = "   selam!  "

#print(metin.strip())

#print()


#print("3. replace()- yer değistirme isine yarar")

#metin = "araba"

#print(metin.replace("a","e"))

#print()


#print("4. find()-harfin veya kelimenin yerini (indexsini) bulur")


#metin = "merhaba phyton, seni seviyorum."

#print(metin. find("a"))

#print()


#print("5. split()- cumleyi kelimelere ayırır")

#metin = "merhaba phyton,seni ögrenmekten zevk duyuyorum"

#kelimeler = metin.split()

#print(kelimeler)

#print()


#print("6. join()- listeyi birlestirir")

#kelimeler = ['phyton','cok','guzel']

#print("".join(kelimeler))

#print()


#print("7. startswith()- hangisiyle baslar?")

#metin ="haci kamaci"


#print(metin.startswith("haci"))

#print()


#print("8. endswith()- sununla bitiyor mu? ")

#metin ="phyton programlama dili"

#print(metin.endswith("dili"))

#print()

#print("9. count()- belirtilen harf kac defa geciyor")

#metin = "seni seviyorum"

#print(metin.count("e"))

#print()


#print("10. isdigit()- sadece rakam mi?")

#print("merhaba".isdigit())

#print("12345".isdigit())

#print("11. isalpha()- sadece harf mi")


#print("merhaba".isalpha())


#print("merhaba12".isalpha())


print("bonus: kullanıcıdan isim al,duzenle,yazdir")


isim = input("adinizi giriniz: ")

isim_duzenli = isim.strip().title()

print("merhaba",isim_duzenli)
