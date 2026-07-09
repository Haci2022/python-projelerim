musteriler = ["hacikamaci", "ademtulgar","serhatkarakoc","yusufkamaci"]
fiyat = [12000,13000,5000,15000]
# 1- ' hacikamaci' kullanıcı adı le yapılan 5000 liralık liralık siparişi listeye ekleyiniz.
musteriler.append("hacikamaci")
fiyat.append(5000)
print(musteriler)
print(fiyat)
#2- son eklenen siparişi siliniz.
musteriler.pop()
fiyat.pop()
print(musteriler)
print(fiyat)
# 3- tüm müşteriler için aşağıdaki özel cümleyi yazınız.
    # <username> isimli musterinin sipariş toplamı <1000> liradır
sonuc = f"{musteriler[1]} isimli musterinin siparis toplami {fiyat[1]} liradir"
print(sonuc)
# 4- müşterileri alfabetik olarak sıralayınız.
musteriler.sort()
print(musteriler)
# 5- sipariş toplamlarını azalan şekilde sıralayınız
fiyat.reverse()
print(fiyat)
# 6- en düşük sipariş hangisidir
sonuc = min(fiyat)
sonuc = max(fiyat)
print(sonuc)
# 7- "hacikamaci" isimli kullanıcının kaç tane siparişi vardır?
sonuc = musteriler.count('hacikamaci')
print(sonuc)
# 8- müşteriler listesinden 'serhatkarakoc' isimli kullanıcıyı siliniz.
musteriler.remove('serhatkarakoc')
print(musteriler)
# 9- listedeki tüm kullanıcıları siliniz
musteriler.clear()
fiyat.clear()
print(musteriler)
print(fiyat)
# 10 - kullanıcıdan aldığınız kullanıcı adı ve sipariş toplamlarını listeye ekleyiniz
isim = input("musteri adini giriniz: ")
toplam = input("toplam: ")
musteriler.append(isim)
fiyat.append(toplam)

print(sonuc)