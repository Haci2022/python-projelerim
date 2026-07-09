

cumle=input("Lütfen bir cümle giriniz: ")

harf=input("Lütfen bir harf giriniz: ")


# önce bütün harfleri küçük harfe çevirelim

harf=harf.lower()

#  cümleyi split fonksiyonu ile kelimelere ayıralım liste gibi 

kelimeler=cumle.split()

# bu adımdan sonra bir sayaç oluştutmamız lazım

sayac=0

#for döngüsü ile sayıyı döndürelim

for kelime in kelimeler:

    if harf in kelime.lower():

        sayac +=1

print(f"{harf} harfini içeren kelime sayısı: {sayac}")
