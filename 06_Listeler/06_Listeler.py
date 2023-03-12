############### LİSTE list() #####################
# Listeler birden fazla veri tutumamızı sağlar.
# Listeler değerleri index(indis) numaralandırma kavramı ile tutarlar.
# Index ilk değere 0 sayısını ve devam eden her değere 1,2,3... numaralar verir.
#
# isimler: list = list()  # Boş bir liste oluştur ve isimler değişkenine ata
# print(type(isimler))
#
# isimler2: list = []  # tavsiye edilmez
#
# ####################### Listeye Veri Ekleme #######################
# # append metodu listeye eleman eklemek için kullanılır
#
# ad: str = "Mehmet"
# yas: int = 29
# maas: float = 38.652
# araba: bool = True
#
# personel: list = list()
#
# personel.append(ad)
# personel.append(yas)
# personel.append(maas)
# personel.append(araba)
# print(personel)
#
# ##### Tavsiye Edilmeyen Yöntem ####
# personel2: list = []
# personel2 += [ad]
# personel2 += [yas]
# personel2 += [maas]
# personel2 += [araba]
# print(personel2)
#
# # Elemanlara ulaşmak
# print(personel[0])
# print(personel.__getitem__(2))  # tavsiye edilen
#
# print(personel)
#
# personel.append("ÖZTÜRK")
# print(personel)
#
# # Listedeki elemanın indis değerine ulaşmak
# print(personel.index("ÖZTÜRK"))
# print(personel.index("ÖZTÜRK", 2))  # Arama işlemine 2. elemandan sonra başla
#
# # İçerdeki bir değerin kaç defa tekrar ettiğini tespit etme
# # count()
# sayilar = [10, 10, 20, 20, 30, 30, 50, 50, 50]
#
# print(sayilar.count(50))
# print(sayilar.count(30))
# print(sayilar.count(20))
# print(sayilar.count(10))
#
# ### Listenin uzunluğunu bulma
# print(len(sayilar))
#
# for sayi in range(len(sayilar)):
#     print(sayilar.__getitem__(sayi))
#     print(sayilar[sayi])
#
# # Listedeki elemanları tek tek yazdırma
# for sayi in sayilar:
#     print(sayi)
#
# for deger in personel:
#     print(deger)

#################### ÖZEL YÖNTEM #################
#
# liste = [1, "Elma", 3, 4, 5, True, 7, 8, 9, 10]
#
# print(liste[-1])  # listedeki son elemana erişmek (tersten)
# print(liste[0:4])  # 0 dan başla 2. elemana kadar git ama 2 yi dahil etme
# ad = "Mehmet"
#
# for harf in ad:
#     print(harf)
#
# print(ad[0:3])
#
# print(ad[2:])
# print(ad[:-3])


# LİSTE SIRALAMA
"""
liste = [1, 9, 8, 3, 99, 12]

liste.sort()  # küçükten büyüğe
print(liste)

liste.sort(reverse=True)  # büyükten küçüğe
print(liste)
"""

import locale

locale.setlocale(locale.LC_ALL, "tr_TR.UTF-8")  # Python  dili Türkçe ayarlanıyor
"""
sehirler = list()
sehirler.append("ZONGULDAK")
sehirler.append("MUĞLA")
sehirler.append("ADANA")
sehirler.append("MALATYA")
sehirler.append("DÜZCE")
sehirler.append("SİVAS")
sehirler.append("İZMİR")
sehirler.append("ŞANLIURFA")
sehirler.append("KAHRAMANMARAŞ")

sehirler.sort(key=locale.strxfrm)
print(sehirler)

#### Listeden değerleri dışarı atma

sehirler.pop()  # Listedeki son elemanı siler
print(sehirler)
sehirler.pop(2)
print(sehirler)

sehirler.remove("DÜZCE")  # listedeki değere göre siler
print(sehirler)

# İstenilen değer içerde var mı ?

if "MALATYA" in sehirler:
    print("Malattya var")
"""
"""
# Kullanıcıdan listeye isim atmasını isteyelim ama tekrar eden değer
# içermesin. Hayır diyene kadar da eklemeye devam etsin

liste: list = list()

while True:
    cevap = input("Listeye eleman eklemek için yazın. Çıkmak için Ç basın").upper()

    if cevap == "Ç":
        break
    else:
        if cevap not in liste:
            liste.append(cevap)

for eleman in liste:
    print(eleman)
    
"""

# LİSTE BİRLEŞTİRME
"""
birinci_yontem_bos_liste: list = list()
ikinci_yontem_bos_liste: list = list()

a: list = [0, 1, 2, 3]
b: list = [4, 5, 6, 7]

# 1. yöntem
birinci_yontem_bos_liste = a + b
print(birinci_yontem_bos_liste)

# 2. yöntem

for eleman in a:
    ikinci_yontem_bos_liste.append(eleman)

for eleman in b:
    ikinci_yontem_bos_liste.append(eleman)

print(ikinci_yontem_bos_liste)
"""
"""
a: list = [0, 1, 2, 3]

referans = 0

for sayi in a:
    if sayi > referans:
        referans = sayi

print(referans)

print(min(a))
print(max(a))
"""
# *** Tek satırda for yazma işlemi ***
"""
sayi_listesi: list = list()

for sayi in range(1, 11):
    sayi_listesi.append(sayi)

print(sayi_listesi)

sayi_listesi_2 = [sayi for sayi in range(1, 11)]
print(sayi_listesi_2)
"""
"""
# SORU 10 ile 100 arasındaki çift sayıları bir listeye atın.

sayi_listesi_2 = [sayi for sayi in range(10, 101, 2)]
print(sayi_listesi_2)
"""

# liste = [44, 33, 55, 66] # adres kadıköy
# liste2 = liste #adres kadıköy
#
# print(liste)
# print(liste2)
# liste.append(77)
#
# print(liste)
# print(liste2)
#
#
#
# a =  [1,2,3] # ram adresi kadıköy
# b = a.copy() # ram adresi mecideköy
#
# print(a)
# print(b)
#
# b.append(4)
#
#
# print(a)
# print(b)

# SORU: Kullanicidan 10 adet sayı alıp listeye
# atın ve sonrasında listenin aritmetik ortalamasını bulun.


# 1. 1-100 arasında 20 adet rastgele sayı üretin ve
# aynı numara içerde olmadan listeye atın.


# SORU: Klavyeden alınan 5 kelimeyi bir listeye atın.
# : Girilen 6. kelimenin listede olup olmadığını ekrana yazdırınız.

"""
sayilar = [10, 40, 30, 40, 40, 20, 20]

### Dizideki elemanın değerini değişmek

sayilar[2] = 15
print(sayilar)
print(sayilar.index(40))  # dizide baştan itibaren 40 değerini ara
print(sayilar.index(40, 3))  # dizide 3. elemandan sonra 40 değerini ara

tekrar: int = 0
for eleman in range(len(sayilar)):
    if sayilar[eleman] == 40:
        print(eleman)
        tekrar += 1

print(sayilar.count(40))
print(tekrar)
"""
"""
sayilar = [10, 40, 30, 40, 40, 20, 20]

sayilar.append(99)
print(sayilar)

sayilar.insert(1, 44)  # indexi 1 olan elemanı sağa kaydır yerine 44 koy
print(sayilar)

sayilar.insert(2, 43)  # indexi 2 olan elemanı sağa kaydır yerine 43 koy
print(sayilar)
"""
# SORU: Kullanicidan 10 adet sayı alıp listeye
# atın ve sonrasında listenin aritmetik ortalamasını bulun.
"""
sayi_listesi: list = list()

for i in range(1, 11):
    sayi = int(input(f"{i}. sayı: "))
    sayi_listesi.append(sayi)

print(sum(sayi_listesi) / len(sayi_listesi))

sayi_listesi_2: list = list()

for i in range(1, 11):
    sayi = int(input(f"{i}. sayı: "))
    sayi_listesi_2.append(sayi)

liste_toplami = 0
for sayi in sayi_listesi_2:
    liste_toplami += sayi

print(liste_toplami / len(sayi_listesi_2))

"""

# 1. 1-100 arasında 20 adet rastgele sayı üretin ve
# aynı numara içerde olmadan listeye atın.
from random import randint

"""

sayilar: list = list()

while len(sayilar) <= 20:
    sayi: int = randint(1, 101)
    if sayi not in sayilar:
        sayilar.append(sayi)

print(sayilar)

"""
"""
sayilar: list = list()

for i in range(1, 30):
    if len(sayilar) <= 20:
        sayi: int = randint(1, 101)
        if sayi not in sayilar:
            sayilar.append(sayi)
        else:
            continue
    else:
        break

print(sayilar)
tek_liste: list = list()
cift_liste: list = list()

for sayi in sayilar:
    if sayi % 2 == 0:
        cift_liste.append(sayi)
    else:
        tek_liste.append(sayi)

print(f"Tek Liste: {tek_liste}")
print(f"Çift Liste: {cift_liste}")
"""
# SORU: Klavyeden alınan 5 kelimeyi bir listeye atın.
# : Girilen 6. kelimenin listede olup olmadığını ekrana yazdırınız.
"""
kelimeler: list = list()
sayac: int = 1

while sayac < 7:
    kelime = input("Bir kelime girin")

    if sayac < 6:
        if kelime not in kelimeler:
            kelimeler.append(kelime)
            sayac += 1
        else:
            print(f"Girmiş olduğunuz {kelime} kelimeler listesinde mevcut")
    else:
        if kelime in kelimeler:
            print(f"{kelime}  kelimesi kelimeler listesinde mevcut")
            break
        else:
            print(f"{kelime}  kelimesi kelimeler listesinde mevcut değil")
            break
"""