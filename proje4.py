isimler=["Ali","Ece","Kaan","Mete","Batu","Veli","Ayşe"]
numaralar=[145,178,164,175,185,180,134]


max_numaralar=0
max_iismler=""


for i in range(len(numaralar)): # 0,1,2,3,4,5,6 sayılarını döndürür

    if numaralar[i]> max_numaralar:
        max_numaralar=numaralar[i]
        max_isimler=isimler[i]

print("En yüksek okul numarası: ",max_numaralar,"sahibi olan öğrenci: ",max_isimler)





# çözüm B

min_numaralar=10**5
min_isimler=""

for i in range(len(numaralar)):
    if numaralar[i]<min_numaralar:
        min_numaralar=numaralar[i]
        min_isimler=isimler[i]

print("en düşük okul numarası: ",min_numaralar,"sahibi olan öğrenci: ",min_isimler)