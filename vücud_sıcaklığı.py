# hastaların ateşini kontrol edin 

sicaklik=float(input("lütfen vücud sıcaklığınızı giriniz:" ))


if(sicaklik<36.1):

    print("vücud sıcaklığı düşük! (Hiptermi riski olabilir!)")

elif(sicaklik<=37.2):

    print("Normal vücud sıcaklığı!")

elif(sicaklik<=38.0):

    print("düşük ateş!!!")

elif(sicaklik<=39.0):

    print(" ateş!")

elif(sicaklik<=40.0):

    print("Dikkat yüksek ateş!!!")


else:

    print("Aşırı yüksek ateş tıbbi yardım alın!!!")



if(sicaklik>=38.0):

    print("Dikkat, yükesek ateş tehlikesi!")

print("Hastanemiz size sağlıklı günler diler...")