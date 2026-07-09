
"""
kullanıcıdan bir kelime alın.
-bu kelimenin tersini ekrana yazdırın.



PROGRAMI İKİ FARKLI YÖNTEMLE YAPIN.
- string dilimleme(slicing) kullanarak
-for döngüsü kullanarak 


"""
"""

kelime=input("Lütfen bir kelime giriniz: ")

ters_kelime=kelime[::-1]

print(ters_kelime)
"""


kelime=input("Lütfen bir kelime griniz: ")

ters_kelime = ""

for harf in kelime:
    ters_kelime = harf + ters_kelime 
    
print(ters_kelime)

