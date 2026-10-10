 
"""
meyveler = ["elma","armut","muz"]
it = iter(meyveler) #iter fonksiyonunu oluşturduk list,str,dict vs gibi şeyler iter fonfisiyonuna aittir

while True:
    try:
        meyve = next(it)
        print(meyveler)
    except StopAsyncIteration:
        break
    
    
print("bye....")
"""
"""
#zip (): 2 veya daha fazla listeyi eşleştirir
isimler=["haci kamaci","serhat karakoç","aybike tutar","yusuf kamaci"]
notlar=[80,100,30,40]
siniflar=["12D","12O","12C","12F"]

sonuçlar=zip(isimler,notlar,siniflar)
sonuc_list=list(sonuçlar)
print(sonuc_list)
"""
"""
#map():bir fonfsyonu listede ki her elemana uygular


def kup_al(x):
    return x**3


sayilar=[1,2,3,4,5,6,7,8,9,10]

sayilarin_karesi_list=list(map(lambda x:x**2,sayilar))
sayilarin_kupu_list=list(map(kup_al,sayilar))
print(sayilarin_karesi_list)
print(sayilarin_kupu_list)
    """
    
#filter():bir koşula göre filtreleme yapar 

def tek_mi(x):
    return x%2==1

sayilar=[1,2,3,4,5,6,7,8,9,10]

çift_sayilar=list(filter(lambda x:x%2==0,sayilar))
tek_sayilar=list(filter(tek_mi,sayilar))
print(çift_sayilar)
print(tek_sayilar)