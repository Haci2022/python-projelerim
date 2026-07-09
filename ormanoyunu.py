def oyunu_baslat():
    """
    Bu fonksiyon, metin tabanlı macera oyununu başlatır ve yönetir.
    Oyunun tüm mantığı bu fonksiyonun içindedir.
    """
    print("--- Ormanda macera oyununa hoş geldin! ---")
    print("Amacın komutları kullanarak ormandan çıkış yolunu bulmak.")
    print("Kullanabileceğin komutlar: ileri, sağa, sola, arkaya, çıkış")

    konum = "baslangic"

    while True:
        if konum == "baslangic":
            print("\nYoğun bir orman içerisindesin. Ne yapacağını bilmiyorsun.")
            print("Önünde bir patika, sağında sık ağaçlar, solunda bir nehir sesi var.")
        
        elif konum == "patika":
            print("\nDar bir patikadasın. Patika 'ileri' ve 'arkaya' doğru uzanıyor.")
            print("Sağında sık ağaçlar, solunda ise nehir var.")
        
        elif konum == "nehir":
            print("\nHızlı akan bir nehrin kenarındasın. Karşıya geçmek imkansız görünüyor.")
            print("Geri dönebilmek için 'sağa' dönebilirsin.")
        
        elif konum == "cikmaz_sokak":
            print("\nSık ağaçların olduğu bir yere geldin. Buradan daha ileriye gidemezsin.")
            print("Geri dönmek için 'sola' dönmelisin.")
        
        elif konum == "cikis":
            print("\nTebrikler! Patikayı takip ederek ormandan çıkış yolunu buldun!")
            print("Oyunu kazandın!")
            break

        # Oyuncudan komut al
        hamle = input("\n> Ne yapmak istersin? ").lower()

        if hamle == "cikis":
            print("\nOyundan çıkılıyor...")
            break

        # Konuma göre hareket mantığı
        if konum == "baslangic":
            if hamle == "ileri":
                konum = "patika"
            elif hamle == "saga":
                konum = "cikmaz_sokak"
            elif hamle == "sola":
                konum = "nehir"
            elif hamle == "arkaya":
                print("\nArkanda sadece daha fazla ağaç var. Farklı yön denemelisin.")
            else:
                print("\nGeçersiz komut! Lütfen geçerli bir yön deneyiniz.")

        elif konum == "patika":
            if hamle == "ileri":
                konum = "cikis"
            elif hamle == "arkaya":
                konum = "baslangic"
            elif hamle == "saga":
                print("\nSık ağaçların arasına giremezsin.")
            else:
                print("\nGeçersiz komut! Lütfen geçerli bir yön giriniz.")

        elif konum == "nehir":
            if hamle == "saga":
                konum = "patika"
            else:
                print("\nNehirden ilerleyemezsin. Geri dönmek için 'sağa' dönmelisin.")

        elif konum == "cikmaz_sokak":
            if hamle == "sola":
                konum = "baslangic"
            else:
                print("\nBuradan ilerleyemezsin. Geri dönmek için 'sola' dönmelisin.")


# Program başlatıldığında oyunu çalıştır
oyunu_baslat()