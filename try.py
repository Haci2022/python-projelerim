# kullanıcıdan bir sayı alıp bunu 10 a bölün ve bu kodu try-except ile yapın 

try:
    sayi=int(input("lütfen bir sayi giriniz: "))
    
    sonuc = 10/sayi
    
    print("sonuc: ",sonuc)
except Exception as e:
   
    print(f"Bir hata oluştu {e}: ")
   
finally: # Hata olsa da olamazasa da çalıştırılacak olan kod bloğudur 
    
    print("İşlem tamamlandi")
    
    #son mesaj
    print("lütfen aldiğiniz hatayi dikkate aliniz!")
    
   
    
 
    
