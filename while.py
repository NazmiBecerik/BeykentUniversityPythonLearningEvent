# sürekli tekrarlanan yapılarda adına loop dediğimiz döngüler kullanırız
"""
print("süper hızlı")
print("süper hızlı")
print("süper hızlı")
"""
"""
    Döngüler Zor Mu? HAYIR. Şunlara Dikkat Edersek Değil
    1→ başlangıç
    2→ bitiş
    3→ artış miktarı
"""
"""
i = 0
while i<300:
    i += 1
    print("süper hızlııııııııııı")
"""


"""
    Döngüler Zor Mu? HAYIR. Şunlara Dikkat Edersek Değil
    1→ başlangıç
    2→ bitiş
    3→ artış miktarı
"""
"""
i = 1
while i<=10:
    print(i, end=" ")
    i +=1
"""


"""
    Döngüler Zor Mu? HAYIR. Şunlara Dikkat Edersek Değil
    1→ başlangıç
    2→ bitiş
    3→ artış miktarı
"""
"""
bu bir sonsuz döngü felaketi
i = 1
while i<=10:
    print(i, end=" ")"""


"""
    Döngüler Zor Mu? HAYIR. Şunlara Dikkat Edersek Değil
    1→ başlangıç
    2→ bitiş
"""

# 1 den 10'a kadar olan sayıları toplayalım
"""
toplam = 0
i = 1
while i<=10:
    toplam += i
    i += 1
print(toplam)
"""

# 5 adet sayı girelim, prog. toplasın
"""
toplam = 0
i = 1
while i<=5:
    sayi = int(input("l. s  giriniz...: "))
    toplam += sayi
    i += 1
print(toplam)
"""


# -1 girene kadar sonsuz döngüde kullanıcıdan sayı alalım, sonunda, prog. toplasın

toplam = 0
sayi = 0
sayi = int(input("l. s  giriniz..., çıkmak için -1: "))
while sayi != -1:
    toplam += sayi
    sayi = int(input("l. s  giriniz..., çıkmak için -1: "))
print(toplam)
