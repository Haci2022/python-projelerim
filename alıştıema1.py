print("---string metotları alıştırmalarına hoşgeldiniz! ---")


# -- alıştırma 1: veri temizleme ve biçimlendirme ---
# görev: aşağıdaki kirli_veri değişkenini al.
# 1. Başındaki ve sonundaki gereksiz boşlukları temizle.
# 2. sadece cümlenin ilk harfini büyük,geri kalanını küççük yap.
# 3.sonucu ekrana yazdır. 
# beklenen çıktı: "Web sitemize hoşgeldiniz."


#kirli_veri = "wEb SiTeMiZe HoŞ gElDiNiZ  "

#print("\n--- alıstırma 1 ---")
#print("orjinal veri: ", kirli_veri)


#çözümü buraya yaz:

#temiz_veri = kirli_veri.strip()
#bicimli_veri = temiz_veri.capitalize()
#print("çözüm: ", bicimli_veri)



# --- Alıştırma 2: Metin değiştirme ve başlıklandırma---
# Görev: aşağıdaki 'makale_başılığı' değişkenini al.
# 1. Her kelimenin ilk harfin büyük yapacak şekilde başlık formatında getir.
# 2. "Sql" kelimesini "postgrestsql" olarak değiştir.
# 3. sonucu ekrana yazdır.
# Beklenen çıktı: "Temel postgressql komıutları ve kullanımı "


#makale_baslıgı = "temel sql komutları ve kullanımı "
#print("\n-- alıstırma 2 ---")
#print("orjinal_baslık : ",makale_baslıgı)


#çözüm

#baslık_formatı = makale_baslıgı.title()
#guncel_baslık = baslık_formatı.replace("sql","postgressql")
#print("cozum: ", guncel_baslık)


print("\n--- alıstırma 3 ---")

#çözümü buraya yaz.

tel_no = input("lutfen bir cep telefonu giriniz: ")

if tel_no.isdigit():

  print("telefon numarası gecerli.")

else: 

    print("lutfen sadece rakam giriniz!")