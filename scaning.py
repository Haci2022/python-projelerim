import socket 


#bu kodda nmap aracı kullanacaz açık varsa sonuç verir yoksa da başarısız olarak bir mesaj döndürür

hedef_site="google.com"
hedef_port=22 #ssh portu

print(f"{hedef_site} adresinden {hedef_port} adresine bağlaniliyor...")

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(5.00) # 5 dakika içerisinde bir sonuç gelmezse pes et

try:
    s.connect((hedef_site,hedef_port))
    
    gelen_mesaj=s.recv(1024).decode("UTF-8")
    
    print(f"BAŞARILI! gelen mesaj şu bilgiyi verdi: ")
    print(gelen_mesaj)
    
except Exception as hata:
    print(f"[-] BAŞARISIZ! gelen mesaj şu hatayi verdi:{hata}") # hata mesajı ne döndürürse onu ekrana yazdırıyor 
    
finally:
    s.close() #oturum burada sonlanıyor 