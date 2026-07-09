kitaplar=[                              
   ("simyacı",180),
   ("1984",200),
   ("şeker portakalı",300),
   ("hayvan çiftliği",353),
   ("mağara",300),
   ("görmek",360),
   ("körlük",390),
          
]
"""
for kitap in kitaplar:
    print(kitap[0],kitap[1])
    """

toplam=0



for kitap_adi, sayfa_sayisi in kitaplar:

    print(kitap_adi, sayfa_sayisi)
    toplam=toplam + sayfa_sayisi
      

print("toplam sayfa sayisi: ", toplam)