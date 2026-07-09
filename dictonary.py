# aşagıdaki öğrenci bilgilerini dictionary listesinde saklayınız 

# 101  yiğit bilgi 2010 (40,80,90)
# 102  ada bilgi 2012 (80,80,80)
# 103  çınar turan 2017 (70,70,70)

#klavyeden girilen öğrencii numarasına göre aşağıdaki cümleyi yazdırınız 
# 101 numaralı yğit bilgi ismindeki öğrencinin yaşı 16 ve not ortalaması 70.



ogrenciler = {

       101:{
           
           "ad":"yigit",
           "soyad":"bilgi",
           "dogumtarihi":"2010",
           "notlar":(40,80,90)

       },

       102:{
           
           "ad":"ada",
           "soyad":"bilgi",
           "dogumtarihi":"2012",
           "notlar":(80,80,80)

       },



       103:{
           
           "ad":"cinar",
           "soyad":"turan",
           "dogumtarihi":"2017",
           "notlar":(90,90,90)


       },


}


ogrenciNo = int(input('ogrenciNo:'))


ogrenci = ogrenciler[ogrenciNo]


ortalama = sum(ogrenci["notlar"])/3

yas = 2026-int(ogrenci["dogumtarihi"])


print(f"{ogrenciNo} numaralı {ogrenci["ad"]} {ogrenci["soyad"]} ismindeki ogrencinin yası: {yas} ve not ortalaması:{ortalama}.")
