# region degiskenler_ilk
"""name = "JHON"
name = "aziz"
print(name)"""
# endregion

# region değişken-isimlendirme-kuralları
# değişken isimlendirme kuralları
"""
    1→ harf veya altı çizili başlamalı
    2→ rakam ile başlayamaz
    3→ ilk harf dışındakiler harf, sayı, alt çizgi olabilir
    4→ alt çizgi dışında alfa sayısal karakterler (%, &...) kullanılmaz
    5→ case sensitive Ad, ad bu ikisi farklı
    6→ python'a özel if, pass, while, def ... bunlar keywords kullanılmaz
    7→ tavs. TR karakter kullanmamaya özen gösterin
"""
"""
#1
birinci = "adana"
_1nci = "adana"
#2
#1nci = "adana"
#3
plaka34= "istanbul"
#4
plaka_34= "istanbul"
#5
ad = "aziz"
Ad = "görkem"
print(ad)
print(Ad)
#6
#def="hjkl"
#7
öğrenci = "ismail"
print(öğrenci)
"""
# endregion

# region notation
# sahada kullanılan 2 adet  değişken tanımlama tarzı
# 1- deve notasyonu
# ogrencininAdiSoyadi
# notOrtalamasi
# 2- alt tire notasyonu
# ogrencinin_adi_soyadi
# not_ortalamasi
# endregion


# concat → değişken birleştirme yada ekrana formatlama
# 1.concat-format yöntemi parametre yöntemi ile
"""okulNumarasi = 1001
ad = "Ali"
soyad = "Kemal"
sinavNotu = 80
print(okulNumarasi, ad, soyad, sinavNotu)
#1001 numarali Ali Kemal'in sınav notu 80
print(okulNumarasi, "numaralı",ad, soyad,"'ın sınav notu", sinavNotu)"""

# 2.concat-format yöntemi + ile
"""
ver = "3.8.3"
os = "xp" #eos
#Windows Versiyonu 10, Python Versiyonu 3.8.3
print("Windows Versiyonu", os, "Python Versiyonu", ver)
print("Windows Versiyonu " +  os + " Python Versiyonu " + ver)"""

# 3.concat-format yöntemi fstring ile
"""baslangicNoktasi = "istanbul"
varisNoktasi = "danimarka"
km = 2800
# istanbul ile danimarka arası mesafe 2800 km dir.
print(f"{baslangicNoktasi} ile {varisNoktasi} arası mesafe {km} dir. {2+3}")"""


# lab
#n1, n2, adSoyad
# Mustafa Çalışkan İsimli Öğrencinin Not Ortalaması 55


# region hesap_makinesi
"""s1 = 10
s2 = 2
print(f"{s1} + {s2} = {s1 + s2}")
print(f"{s1} - {s2} = {s1 - s2}")
print(f"{s1} * {s2} = {s1 * s2}")
print(f"{s1} / {s2} = {s1 / s2}")"""
# endregion

#region steak-heap-davranışı
"""a = 2
b = a
a = 10
print(b)"""
#?b = a demek, a'nın değeri değiştiği anda b demi değişecek (cevap hayır)
#endregion"

#region yer_degistirme
#değişken yer değiştirme, sıralama algoritması
"""
a = 10
b = 20
temp = a
a = b
b = temp
print(a, b)"""
"""
a = 10
b = 20
a, b = b, a
print(a, b)"""
#endregion
"""
saat = 2
saniye = 3600
print(f"Saat → {saat}")
print(f"Ekrandaki saat biriminin saniye karşılığı→  {saat*saniye}")"""

#shortcut operatörleri +=, -=, *=, /=
"""
sayi = 10
sayi = sayi + 1     # sayi += 1
print(sayi)"""

#lab
skor = 0
can = 3
skor += 1
can -= 1
print(f"anlık skorunuz {skor}")
print(f"kalan canınız {can}")

