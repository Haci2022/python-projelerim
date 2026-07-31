kullanici_liste = [ 10,'x',3,'y',5]
gecerli_sayilar= [1,2,3,4,5,6,7,8,9,10]

for i in kullanici_liste:
    try:
     if i not in gecerli_sayilar:
        raise ValueError(f"Hata: {i} geçersiz bir değer girdiniz! lütfen daha sonra tekrar deneyiniz...")
    except ValueError as e :
        print("istisna yakalandi: ",{e})
        
        continue
    
    print(f"{i} sayisinin karesi : {i**2}")     # hata alınmazasa burası çalışır 
    
    