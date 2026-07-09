# for dngüsü

meyveler = ["kiraz","seftali","elma","armut","uzum","portakal"]

numara = (70,19,34,23,7)


sayi = int(input("lutfen bir tam sayi giriniz:"))


for item in  range (sayi):

    if(item%2==1):

        continue

    print(item,end="")

else:

    print("\n for dongusu bitti!")