#region Karar Verme
#karşılaştırma operatörleri
"""
==  eşit mi
<   küçük mü
>   büyük mü
<=  küçük eşit mi
>=  büyük mü
!=  eşit değil mi

lütfen karıştırmayın!!!!
= ve == aynı değil
!= olmalı =! değil
"""
"""
print(5==5)
print("istanbul"=="İstanbul")
print(10 == 10.0)
print("-"*50)  #bunu 50 kez (*) tekrarla
print(5 != 4)
print(5 != 5)
print(4<5)
print(5<4)
print("-"*50)  #bunu 50 kez (*) tekrarla
print(5>4)
print(4>5)
print(4<=5)
print(5<=5)
print(5>=6)

yas = int(input("yaşınınız: "))
print(yas>=18)"""
#endregion

#region 1. Örnek
"""
havaDurumu = "yağmurlu"
print("if den önce")
if havaDurumu == "yağmurlu":
    print("şemsiyeni al")
print("if den sonra")
"""
"""
a = int(input("lütfen sayı giriniz: "))
if a<0:
    print(f"{a} sayısı negatiftir")"""
#endregion

#region 2. Örnek
"""
    Mutlak Değer Hesaplayan Python Prog.
    Lütfen Mutlak Değeri Alınacak Sayı Giriniz: 5
    Mutlak Değeri → 5

    Lütfen Mutlak Değeri Alınacak Sayı Giriniz: -15
    Mutlak Değeri → 15
"""

"""
a = int(input("lütfen mutlak değeri alınacak sayı giriniz : "))
if a<0:
    a = a*(-1)
print(a)"""
#endregion

n1 = int(input("lütfen 1. snv notunuzu giriniz... : "))
n2 = int(input("lütfen 2. snv notunuzu giriniz... : "))
n3 = int(input("lütfen 3. snv notunuzu giriniz... : "))
ort = (n1+n2+n3)/3
if ort>=50:
    print(f"GEÇTİNİZ. Sınavlarınızın Ortalaması {round(ort, 2)}")