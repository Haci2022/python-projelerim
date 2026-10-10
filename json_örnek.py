#json.loads() ve json.dumps() Metodları 

#json.loads() - JSON string'ini python nesnesine dönüştürme 
"""
import json 
json_string='{"ad":"haci","yaş":21,"diller":["Python","C++"]}'
# JSON stringini bir python dict(sözlüğüne) çevir
veri = json.loads(json_string)
print(veri)
print(veri["ad"])
print(veri["diller"])
print("hacinin bildiği dil sayisi: ", len(veri["diller"]))
print(veri["diller"][0])
"""
import json
# json.dumps() - python nesnesini JSON string'e dönüştürür
ogrenciler = {
    "ogrenciler": [     
    {
        
        "ad":"ömer",
        "yaş":21,
        "dersler":["matematik", "fizik"]
    },
    {
        "ad":"ayşe",
        "yaş":22,
        "dersler":["edebiyat","kimya"]
    }   
    ] 
    
}
#dict=> JSON string'e dönüştürelim
json_string= json.dumps(ogrenciler,ensure_ascii=False, indent=2)
my_obj=json.loads(json_string)
print(my_obj["ogrenciler"][0]["yaş"])
