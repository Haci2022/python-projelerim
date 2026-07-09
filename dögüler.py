#döngüler ve koşullu işlemler

def menu():

    print("\n ---python mini uygulama---")
    print("1-1'den 20'ye kadar sayiari yazdir")
    print("2- carpim tablosu")
    print("3- uygulamadaki 'a' harfi sayisi")
    print("4- en buyuk sayi bul")
    print("5- programdan cik ")

    while True:
        menu()

        secim= input("seciminiz:")

        #sayıları listeleme 

        if secim =="1":

            for i in range(1,21):
                print(i)

                # 2. koşula geçiş

        elif secim=="2":

            n = int(input("hangi sayinin carpim tablosu:"))

            for i in range(1,11):

                print(f"{n} x {i} = {n*i}")


                # 3. seçime geçiş

                metin = input("bir metin giriniz: ")

                sayac = 0

                for harf in metin.lower():

                    if harf=="a":

                        sayac+=1

                        print(f"'a' harfi sayisi:{sayac}")

                    elif secim =="4":
                        adet=int(input("kac sayi gireceksiniz: "))

                        sayilar = []

                        for i in range(adet):

                            s=int(input(f"{i+1}.sayi:"))

                            sayilar.append(s)

                            en_buyuk = sayilar[0]


                            for s in sayilar:

                                if s>en_buyuk:

                                    en_buyuk = s

                                    print("en buyuk sayi: , en_buyuk")



                                elif secim == "s":

                                    print("programdan cikiliyor...")
                                    break

                                else:

                                    print("hatali secim yaptiniz. tekrar deneyiniz!")

                                     


                        

            





        