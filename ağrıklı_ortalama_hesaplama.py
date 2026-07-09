"""
PYTHON KODLAMA PROJESİ 

agirlikli_ortalama_hesapla(mt1, mt2, f) isimli bir Python fonksiyonu yazınız. 

1. Bu fonksiyon üç sınav sonucunu alır (100 üzerinde notlar girilecek) ve ağırlıklı ortalamayı hesaplar.

2. Sınavların ağırlıkları sırasıyla %20, %35 ve %45 olarak verilmiştir. 

3. Ortalamayı ekrana yazdırın

4. Ayrıca eğer ortalama notu 50'den küçükse veya final notu 20'den küçükse 
   (midterm notları ne olursa olsun) bütünlemeye kaldınız yazsın, aksi takdirde geçtiniz yazsın.
"""




def agirlikli_ortalama_hesapla(mt1,mt2,f):
    
    ortalama=(mt1*0.20)+(mt2*0.35)+(f*0.45)

    print("ortalama: ",ortalama)


    if ortalama < 50 or 20:

        print("Bütünlemeye kaldınız!")

    else:

        print("Tebrikler geçtiniz!")


agirlikli_ortalama_hesapla(80,55,20)

