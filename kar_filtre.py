def kar_filtrele(kelimeler):

    sonuc=[]

    for kelime in kelimeler:

        if "kar" in kelime:

            sonuc.append(kelime)

    return sonuc



kelimeler=["karpuz","elma","armut","kardanadam","güneşli hava","kayak","kar yağışı"]

print(kar_filtrele(kelimeler))



# list comprehension 

def kar_filtre(kelimeler):

    return[kelime for kelime in kelimeler if "kar" in kelime]  # "kar" kelimesi geçen yerleri filtreler

kelimeler=["karpuz","elma","armut","kardanadam","güneşli hava","kayak","kar yağışı"]

