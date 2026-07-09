# docx metni okuma işlemi yapar.

import re
from collections import Counter


def read_docx_words(path):
    doc=doc(path) # verilen dosyayı açar

    text = ""

    for para in doc.paragraphs:

        text+=" "+para.text   # işlenilecek döngü

        # kelimeleri temizleme bölümü 


        words = re.findall(r"[a-zA-ZğüŞöçıiĞüşöÇ]+",text.lower()) #harflerin büyük veya küçük olduğunu belirtmek için kullanılan kod parçacığı


    def get_kelime_analizi(words):


     counter = Counter(words)          #tekrar edilecek 100 kelime bu kod bloğunda bulunur 


    return counter.most_common(100) # type: ignore