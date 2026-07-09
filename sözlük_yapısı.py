#python dicitonary(sözlük) veri yapısı 
#dicitonary fonksiyonunda veri eklemek için "ogrenciler_dict[...]="isim" 
# öğrenci çıkarmak için ise pop() fonksiyonu kullanılır=> öğrenciler_dict.pop(öğrenci numarası)"
#del ile de öğrenci çıkarılabilir.
# mutable=> ogrenciler_dict[numara]=>"başka bir isim"


ogrenciler_dict = {100:"serhat karakoç",101:"haci kamacı",102:"mazlum karakoç",103:"ahmet kamacı",104:"bahar kamacı"}

deger=ogrenciler_dict.get(102)


if deger is None:

    print("Aranılan öğrenci okulda yok!")

else:

    print("öğrenci okulda kayıtlı..")

list1=list(ogrenciler_dict.keys())
list2=list(ogrenciler_dict.values())

print(list1)
print(list2)