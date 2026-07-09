# list.py dosyan
gorevler = []

# Bu satır en solda
while True:
    # BU BLOKTAKİ HER ŞEY BİR SEVİYE İÇERİDE (1 Tab)
    secim = input("ne yapmak istersiniz ? (ekle/listele/cikar): ")

    if secim == "ekle":
        # Bu satır BİR SEVİYE DAHA İÇERİDE (Toplam 2 Tab)
        yeni_gorev = input("Eklenecek görevi yazın: ")
        gorevler.append(yeni_gorev)
        print(f"'{yeni_gorev}' listeye eklendi!")
        print("---------------------------")

    elif secim == "listele":
        # Bu bloktaki kodlar da bir seviye daha içeride olmalı
        print("--- Yapılacaklar Listesi ---")
        if len(gorevler) == 0:
            print("Listeniz şu anda boş.")
        else:
            for gorev in gorevler:
                print("- " + gorev)
        print("---------------------------")

    # Diğer bloklar da aynı şekilde...
    elif secim == "cikis":
        print("programdan cikis yapiliyor hocakaliniz")
        break

    else:
        print("gecersiz komut! lutfen 'ekle', 'listele' veya 'cikis' yaziniz!")
        print("---------------------------")