
# SET (küme) veri yapısı
#set veri yapısında "add()" fonksiyonu ile veriler eklenilebilir ve "remove" komutu ile de eklenen veriler çıkarılabilir.

muh_dersleri_set = {"Tarih","Matematik","Kimya","Fizik"}  #unordered elemanlar unique
sanat_dersleri_set ={"Tarih","Coğrafya","Piyano","Resim"}



# kesişim(intersection)

ortak_dersler_set=muh_dersleri_set.intersection(sanat_dersleri_set)
print(ortak_dersler_set)

#fark(difference)

print(muh_dersleri_set.difference(sanat_dersleri_set))
print(sanat_dersleri_set.difference(muh_dersleri_set))



#birleşim(union)

birleşim=muh_dersleri_set.union(sanat_dersleri_set)
print("Birleşim seti:", birleşim)


# list ve set veri yapılarını kullanarak aşağıda verilen listedeki tekrar eden (duplicate) elemanları silip
# aynı isimde ama bu sefer içinde tekrar eden eleman olmayan bir liste haline dönüştürünüz.


sayilar_list=[1,2,3,4,3,2,5,6,7,5,2,6,7,8,9,8]

sayilar_set=set(sayilar_list)

print(sayilar_set)