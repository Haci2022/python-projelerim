"""
dosya =open("ornek.txt ", encoding="utf-8")

#dosya okuma işlemi 

icerik = dosya.read()
print(icerik)
dosya.close()
"""
"""

mod       anlamı
==============================
r         okuma işlemi için kullanılır 
w         dosyayı yazmak için açar,eski dosyayı siler
a         dosyaya ekleme yapmak için kullanılır 
r+        dosyayı em okumak hem de yazmak için kullanılır 

"""
"""
try:
    with open("ornek.txt", "w", encoding="utf-8") as dosya:
        dosya.write("python çok eğlenceli bir yazilim dili\n")
        dosya.write("dosya okuma ve yazma bu program ile çok kolay\n")
        
except FileNotFoundError:
    print("hata dosya bulunamadi")
except IOError:
    print("hata dosyasi okunurken bir hata oluştu")
except Exception as e:
    print(f"bilinmeyen bir hata oluştu: {e}")
    
    
    print("bye...")
"""
with open("ornek.txt","r",encoding="utf-8") as dosya:
    satirlar=dosya.readlines()
    
    #strip()=> bir stringin başındaki ve sonundaki gereksiz boşlukları ve karakterleri temizler
    
    temiz_satirlar=[satir.strip() for satir in satirlar]
    
    
    print(temiz_satirlar) 