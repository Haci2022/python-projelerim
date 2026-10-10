#json.load() ve json.dump metodları 
"""
import json
# JSON stringindeki çift tırnak hatası düzeltildi
json_string='{"ad":"haci","yaş":21,"diller":["Python","C++"]}'

# JSON stringini bir python dict(sözlüğüne) çevir
veri = json.loads(json_string)

print(veri)
# Hatalı olan veri("ad") yerine veri["ad"] kullanıldı
print(veri["ad"])
# Hatalı olan veri("diller") yerine veri["diller"] kullanıldı
print(veri["diller"])

print("hacinin bildiği dil sayisi: ", len(veri["diller"]))
print(veri["diller"][0])
import json
ogrenciler = {
    "ogrenciler": [
    {
        "ad":"haci",
        "yaş":21,
        "dersler":["kimya","fizik"]
    },
    {
        "ad":"esma",
        "yaş":20,
        "dersler":["ingilizce","edebiyat"]
        
    }
    ]
}
"""
import json
dosya_adi="ornek_ogrenciler.json"

#JSON dosyasına yazma  (dump)
"""
with open(dosya_adi,"w",encoding="utf-8") as dosya:
    json.dump(ogrenciler,dosya,ensure_ascii=False, indent=2)
    
    print(f"{dosya_adi} dosyasina JSON olarak yazildi!")
 """ 
 
 # JSON dosyasını okuma (load)
 
with open(dosya_adi,"r",encoding="utf-8") as dosya:
     okunan_veri=json.load(dosya)
     
     
ogrenci_listesi=okunan_veri["ogrenciler"]
ogrenci_sayisi=len(ogrenci_listesi)

toplam_yas=0


for ogrenci in ogrenci_listesi:
    toplam_yas=toplam_yas+ogrenci["yaş"]
    
ortalama=toplam_yas/ogrenci_sayisi

print("ortalama:",ortalama)
    