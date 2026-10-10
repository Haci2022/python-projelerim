import socket 


target="Hedef_ip"  #hedef makinenin ip adresi buraya grilir 
ports=[20,21,22,23,24,25,53,68,80,110,443] #kullanacağımız port adresileri 

print(f"---{ports} taraniyor...")

# listeler daha iyi gezebilmek için for döngüsünü kullannıyoruz
for port in ports:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(2.00)  # tarama dakikasını belirliyoruz 
    
    result=s.connect_ex((target,port))
    
    if result==0:
        print(f"[+] {port}: AÇIK")
    else:
        print(f"[-] {port}: KAPALI")
    s.close()

