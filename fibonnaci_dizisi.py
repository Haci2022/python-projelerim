def fibonacci():
    n=int(input("Lütfen bir sayı giriniz (2'den büyük olmalı): "))


    if n <=2:

        print("2'den büyük bir sayı girerek devam edin lütfen!")
        return
    
    fib_serisi=[]
    a=0
    b=1

    while a <= n:

        fib_serisi.append(a)

        #Geçici terimleri kullanarak güncelle

        temp=a+b
        a=b
        b=temp
    
    print("fibonacci serisi: ",fib_serisi)

fibonacci()