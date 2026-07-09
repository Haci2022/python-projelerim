import requests
import os
import time
import hashlib
#bütün bitkileri bir anda dindir
SEARCH_TERMS = ["Caulerpa", "Caulerpa racemosa", "Caulerpa taxifolia", "Caulerpa cylindracea"]
MAX_IMAGES = 1500
OUTPUT_FOLDER = "wikimedia_caulerpa"
DELAY = 1.0
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
})
downloaded = 0
offset = 0
print("Wikimedia Commons'tan Caulerpa fotoğrafları indiriliyor...")
while downloaded < MAX_IMAGES:
    for term in SEARCH_TERMS:
        if downloaded >= MAX_IMAGES:
            break
            #veri url 
        url = "https://commons.wikimedia.org/w/api.php"
        params = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": term + " underwater OR diving OR reef",
            "srnamespace": 6,        
            "srlimit": 50,
            "sroffset": offset
        }
        
        try:
            response = session.get(url, params=params, timeout=30)
            data = response.json()
            
            results = data.get("query", {}).get("search", [])
            if not results:
                continue
            for item in results:
                if downloaded >= MAX_IMAGES:
                    break
                    
                filename = item["title"]
                if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                    continue
                file_url = f"https://commons.wikimedia.org/wiki/Special:FilePath/{filename.replace(' ', '_')}"
                
                try:
                    
                    img_response = session.get(file_url, timeout=40, allow_redirects=True)
                    if img_response.status_code != 200:
                        continue
                    
                    real_url = img_response.url
                    
                    save_name = f"wiki_{downloaded:05d}_{filename.replace('File:', '').replace(' ', '_')}"
                    filepath = os.path.join(OUTPUT_FOLDER, save_name)
                    
                    if os.path.exists(filepath):
                        continue
                    
                    print(f"İndiriliyor ({downloaded + 1}/{MAX_IMAGES}) - {term}")
                    final_img = session.get(real_url, timeout=40)
                    if final_img.status_code == 200:
                        with open(filepath, "wb") as f:
                            f.write(final_img.content)
                        downloaded += 1
                        
                except:
                    continue
                    
        except Exception as e:
            print(f"Hata: {e}")
            time.sleep(5)
            continue
    #toplam
    print(f"Progress → Toplam indirilen: {downloaded}")
    offset += 50
    time.sleep(DELAY)
#bitti
print(f"\n✅ Tamamlandi! Toplam {downloaded} fotoğraf indirildi.")