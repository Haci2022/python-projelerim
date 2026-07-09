# aşağdaki müşterinin bilgilerini ve satın aldığı ürün bilgilerini değişkenler içerisinde saklayınız. Toplam ödenecek tutar nedir? 
# ödenecek miktarın kdv oranı nedir? (%20)

# haci kamaci
# 05372932229
# khaci@gmail.com
# diyarbakır bağlar

# satın alınan ürünler:
# ürün adı: ceket  
# ürün fiyatı:1200 tl

# ürün adı: ayakabı 
# ürün fiyatı: 5000 tl 

# ürün adı: kazak 
#ürün fiyatı: 2000 tl


musteriad = "haci"
musterisoyad = "kamaci"
musterimail = "khaci@gmail.com"
musteriadres = "diyarbakir baglar"


# satın alınan ürünler 

urun1adi = "ceket"                                     # str: karakter tabanlı matematiksel işlem için kullanılır
urun1fiyat = 1200


urun2adi = "ayakabi"
urun2fiyat = 5000

urun3adi = "kazak"
urun3fiyat = 2000


toplamOdenecektutar  =urun1fiyat + urun2fiyat + urun3fiyat   


print("toplam odenen miktar:  "+ str(toplamOdenecektutar))
print("toplam odenen kdv miktari:" + str(toplamOdenecektutar*0.20))

