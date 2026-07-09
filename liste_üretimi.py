
"""
sayilar=[1,2,3,4,5,6,7,8,9,10]
ciftler=[]

for x in sayilar:

    if x % 2 ==0:

        ciftler.append(x)

print(ciftler)
        """

"""
sayilar=[1,2,3,4,5,6,7,8,9,10]
ciftler=[]

ciftler= [x**2 for x in sayilar if x % 2 == 0]
print(ciftler)

"""

kelimeler=["python","java","c++","sql","html"]

buyuk_harfler=[]


for kelime in kelimeler:
    buyuk_harfler.append(kelime.upper())

print(buyuk_harfler)


#list comprehension ile

buyuk_harfler=[kelime.upper() for kelime in kelimeler]

print(buyuk_harfler)