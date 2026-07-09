#kullanıcıdan ismini ve şifreini alıp sisteme giriş yapmasını sağlayan kod 


kullanici_adi=input("Lütfen kullanıcı adınızı giriniz:")

sifre=input("Lütfen şifrenizi giriniz: ")


if kullanici_adi =="KALİ" and sifre == "LİNUX":

    print("Sisteme giriş başaşrılı! Hoşgeldiniz...")


else:

    print("Hatalı kullanıcı adı veya şifre! Giriş başarısız!")