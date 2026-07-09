""" 
PYTHON PROJE #5
- - - - - - - -
Kullanıcının iki sayı girerek toplama, çıkarma, çarpma ve bölme işlemlerini yapabileceği bir
hesap makinesi programı yazın. Program şu özelliklere sahip olmalıdır:

Kullanıcıya yapmak istediği işlemi seçmesi için bir menü sunulmalıdır:

1. Toplama
2. Çıkarma
3. Çarpma
4. Bölme
5. Çıkış
Kullanıcı geçerli bir işlem seçtikten sonra iki sayı girmesi istenmelidir.

İşlem sonucu ekrana yazdırılmalıdır.

Kullanıcı 5 girerek çıkış yapmadıkça program sürekli çalışmalıdır.

Bölme işleminde sıfıra bölme durumu kontrol edilmelidir.
"""




print("HESAP MAKİNESİNE HOŞGELDİNİZ!")



while True:

    print("\n-----MENÜ-----")
    print("1.Toplama")
    print("2.Çıkarma")
    print("3.Çarpma")
    print("4.Bölme")
    print("5.Çıkış")

    secim=input("Yapmak istediğiniz seçimi giriniz(1-5): ")

    if secim==5:

        print("Programdan çıkılıyor... Hoşçakalın!")
        break

    if secim  in ["1","2","3","4"]:

        sayi1=int(input("Lütfen ilk sayıyı  giriniz: "))
        sayi2=int(input("Lütfen ikinci sayıyı giriniz: "))


    if secim=="1":
        print(f"{sayi1}+{sayi2}={sayi1+sayi2}")
    
    if secim=="2":
        print(f"{sayi1}-{sayi2}={sayi1-sayi2}")

    if secim=="3":
        print(f"{sayi1}x{sayi2}={sayi1*sayi2}")

    if secim=="4":
        if sayi2==0:

            print("Hata! Bir sayı sıfıra bölünmez.")
        else:
            print(f"{sayi1}/{sayi2}={sayi1/sayi2}")

else:

    print("Geçersiz işlem! 1 ila 5 arasında sayı girmelisiniz.")

print("Hoşçakalınn...")



