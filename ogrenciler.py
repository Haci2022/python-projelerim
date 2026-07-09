# 1- aşağıdaki  verileri liste içerisinde saklayınız.

#  öğrenci1: serhat karakoç 2005 [70,80,90]
# öğrenci2: haci kamacı     2005  [80,90,70]
# öğrenci3: adem tulğar     2000 [60,70,80]


ogrenci1 = ["serhat", "karakoc", 2004, [70, 80, 90]]
ogrenci2 = ["haci", "kamaci", 2005, [80, 90, 70]]
ogrenci3 = ["adem", "tulgar", 2001, [60, 70, 80]]

ogrenciler = [ogrenci1, ogrenci2, ogrenci3]

print(ogrenciler)




# 10- ögrencilerin yaşlarını hesaplayınız 

yasserhat = 2025 - ogrenciler[0][2]

yashaci =  2025 - ogrenciler[1][2]

yasadem  = 2025 - ogrenciler[2][2]

print(yasserhat,yashaci,yasadem)



# öğrencilerin not ortalamasını giriniz.

notserhat =(ogrenciler[0][3][0] + ogrenciler[0][3][1] + ogrenciler[0][3][2])/ 3

nothaci = (ogrenciler[0][3][0] + ogrenciler[0][3][2] + ogrenciler[0][3][2])/ 3

notadem = (ogrenciler[0][3][0] + ogrenciler[0][3][2] + ogrenciler[0][3][2])/ 3

print(notserhat,nothaci,notadem)

