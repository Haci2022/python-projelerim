kitaplar=[
      ("sokratesin savunması",200),
      ("şeker portakalı",152),
      ("1984",352),
      ("devlet",360),
      ("kuyucaklı yusuf",251),
      ("ateşten gömlek",201),
      ("hayvan çiftliği",150),

]

fazla_sayfa_kitaplar=[]

toplam_sayfa=0


for kitap_adi, sayfa_sayisi in kitaplar:

    if sayfa_sayisi > 170:

        fazla_sayfa_kitaplar.append(kitap_adi)

        toplam_sayfa+=sayfa_sayisi

print("\n 170'ten fazla sayfaya sahip olan kitaplar: ")

for kitaplar in fazla_sayfa_kitaplar:

    print(kitaplar)

print("toplam sayfa: ",toplam_sayfa)