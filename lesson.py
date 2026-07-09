#isim=input("lutfen adinizi giriniz: ")

#print("merhaba",isim)








#sayi1=int(input("lutfen birinci sayiyi giriniz:"))



    #sayi2=int(input("lutfen ikinci sayiyi giriniz:"))



#toplam=sayi1+sayi2


     #print("toplam:",toplam)




sifre ="7652" # aranan şifre 

flag = False


for basamak1 in range(10):
    for basamak2 in range(10):
        for basamak3 in range(10):
            for basamak4 in range(10):

                deneme = str(basamak1) + str(basamak2) + str(basamak3) + str(basamak4)
                print(deneme) # denenen şifreyi yazdır

                if deneme ==sifre:
                    print("parolaniz bulundu:",deneme)

                    flag=True
                    break  #en içteki dögüyü kırar

                if flag:

                    break
                if flag:

                    break
                if flag:

                    break
 


