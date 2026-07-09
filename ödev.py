def cift_sayilar_dondur(sayilar):
    return[x for x in sayilar if x % 2 == 0]  # list comphrehension tekniği
sayilar=[0,1,2,3,4,5,6,78,9,10]
sonuc=cift_sayilar_dondur(sayilar)
print("çift sayılar:",sonuc)

