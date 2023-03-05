##### FOR DONGUSU #####

"""
for sanal_degisken adi in sayılabilir_aralıgı:
        yapılacak işlemleri
"""

# 0-10
# range(5) => # 0-5
"""
print(range(5))  # 0-5 aralığı başlangıç ve bitişler alınmaz
print(range(1, 5))  # 1-5 aralığı  bitişler alınmaz
print(range(1, 9, 3))  # 1,4,7  bitişler alınmaz

for sayi in range(1, 11):
    print(sayi)

for sayi in range(1, 9, 3):
    print(sayi)

for harf in "Kadıköy":
    print(harf)
"""
"""
## SORU 20-40 arasındaki çift ve tek sayıların
# toplamlarını ayrı ayrı ekrana yazdırınız.
tek_toplam: int = 0
cift_toplam: int = 0

for sayi in range(20, 41):
    if sayi % 2 == 0:
        cift_toplam += sayi
    else:
        tek_toplam += sayi

print(f"Tek Sayıların Toplamı: {tek_toplam}")
print(f"Çift Sayıların Toplamı: {cift_toplam}")
"""
# 1'den başlayarak Klavyeden girilen sayıya kadar
# olan sayılardan 4'e tam bölünenlerinin çarpımını yazdırınız
"""
carpim: int = 1
sayi: int = int(input("Lütfen bir sayı giriniz: "))

for i in range(1, sayi + 1):
    if i % 4 == 0:
        carpim *= i
print(f"1-{sayi} arasındaki sayıların 4 e tam bölenlerinin çarpımı: {carpim}")
"""
# Kullanıcıdan girilen sayıya kadar olan sayıların çarpımını
# hesaplayın (Faktöryel Hesabı) 1-5 1.2.3.4.5
"""
carpim: int = 1

baslangic: int = int(input("Başlangıç: "))
bitis: int = int(input("Bitiş: "))

if baslangic <= 0:
    baslangic = 1

if bitis <= 0:
    bitis = 1

for elma in range(baslangic, bitis+1):
    carpim *= elma

print(f"{baslangic}-{bitis} aralığındaki sayıların çarpımı: {carpim}")

"""

############ PRINT ÖZEL KOMUTLAR ##############
#
# print(" Elma" * 2)
# print("*" * 148)
#
# print("G", "F", end="")  # Sondaki karakteri sil
# print("A")  # \n
# print("20", "11", "1993", sep=".")  # Yapılar arasına istenilen karakteri atar
#
# ### Kaçış Karakterleri
#
# #  \ Ters slash
#
# # Bu gün "Ahmet" gelmedi
# print("Bu gün \"Ahmet\" gelmedi")
#
# print("""
# Ahmet "Gelsin" banane "ben" evdeyim
# """)
#
# print("İstanbul'un merkezi \"anadolu\" 'dur")
#
# # \n Yeni Satır
#
# print("Ben\nBu\nGün\nGelmicem")
#
# baslik = "Kitap Başlığı"
#
# print(baslik, "@" * len(baslik))
#
# # \t Tab 4 boşluk atar
# print("Merhaba\t\tDünya")
# print(*"123456789", sep="\t")
# # \a Zil çalar
# print("\a" * 10)
#
# # \r Aynı Satır Başı
# print("Merhaba\rZalım Dünya")
#
# # Düşey Sekme (\v)
# print("düşey\vsekme")
#
# # İmleç Kaydırma (\b)
#
# print("herseymi.com\b.uk")

# Kaçış Dizisi	Anlamı
# ‘	Karakter dizisi içinde tek tırnak işaretini kullanabilmemizi sağlar.
# “	Karakter dizisi içinde çift tırnak işaretini kullanabilmemizi sağlar.
# \	Karakter dizisi içinde \ işaretini kullanabilmemizi sağlar.
# \n	Yeni bir satıra geçmemizi sağlar.
# \t	Karakterler arasında sekme boşluğu bırakmamızı sağlar.
# \u	UNICODE kod konumlarını gösterebilmemizi sağlar.
# \U	UNICODE kod konumlarını gösterebilmemizi sağlar.
# \N	Karakterleri UNICODE adlarına göre kullanabilmemizi sağlar.
# \x	Onaltılı sistemdeki bir sayının karakter karşılığını gösterebilmemizi sağlar.
# \a	Destekleyen sistemlerde, kasa hoparlöründen bir ‘bip’ sesi verilmesini sağlar.
# \r	Aynı satırın başına dönülmesini sağlar.
# \v	Destekleyen sistemlerde düşey sekme oluşturulmasını sağlar.
# \b	İmlecin sola doğru kaydırılmasını sağlar
# \f	Yeni bir sayfaya geçilmesini sağlar.
# r	Karakter dizisi içinde kaçış dizilerini kullanabilmemizi sağlar.


"""
*
**
***
****
*****
"""
# for i in range(1, 7):
#     print("*" * i)

"""
*****************
*               *
*               *
*               *
*               *
*****************
"""

# for i in range(1, 10):
#     if i == 1 or i == 9:
#         print("*" * 17)
#     else:
#         print("*", (" " * 15), "*", sep="")

"""
            *
           ***
          *****
         *******
        *********
"""
# sayac: int = 1
# for satir in range(1, 20):
#     print(" " * (20 - satir), end="")
#     print("*" * sayac)
#     sayac += 2

## ÇARPIM TABLOSU

"""
1 x 1 = 1 1 x 2 = 2 1 x 3 =3
2 x 1 = 2 ....
3 x 1 = 3 
"""
# for i in range(1, 11):
#     for j in range(1, 11):
#         # print(i, "*", j, "=", (i * j), end="\t\t\t")
#         print(f"{i}*{j}={i * j}", end="\t\t\t")
#     print()
#
# for i in range(10, 0, -1):
#     print(i)

#### TAHMİN OYUNU ####
# Bilgisayar 1-100 arasında rastgele bir sayı üretsin.
# Kullanıcının 5 hakkı olsun ve sayıyı bilmeye çalışsın.
# Bilirse TEBRİKLER. bilemezse tekrar deneyiniz. hakkı biter hakkınız bitti yazsın.
# BONUS: tahmin değeri rastgele değerden büyük ise tahmininizi küçültünüz
#        tahmin değeri rastgele değerden küçük ise tahmininizi büyültünüz
"""
import random

rast_gele_sayi: int = random.randint(1, 100)

for hak in range(1, 6):

    tahmin: int = int(input("Tahmin Ettiğiniz Sayıyı Giriniz: "))

    if tahmin > rast_gele_sayi and hak < 5:
        print("Lütfen tahmin değerinizi küçültün! 😒 ")
    elif tahmin < rast_gele_sayi and hak < 5:
        print("Lütfen tahmin değerinizi büyültün! 😒")
    elif tahmin == rast_gele_sayi:
        print("Tebrikler ! 🥳")
        break
    else:
        print("😛 Takkınız Bitti")
        print("Üretilen Sayı: ", rast_gele_sayi)
"""

"""
# SORU: Kullanıcıdan personel sayısını alınız.
# Personelin kaç çocuğu olduğunu isteyelim.
# Program her çocuk için "Çocuğunuz adına 1 ağaç dikilmiştir" yazsın
# Toplam dikilen ağaç sayısınıda ekrana yazdıralım.
"""
toplam_dikilen_agac_sayisi: int = 0
personel_sayisi: int = int(input("Persnel Sayınızı Giriniz: "))

for personel in range(1, personel_sayisi + 1):

    while True:
        cocuk_sayisi = int(input(f"{personel}. personelin çocuk sayısı: "))
        toplam_dikilen_agac_sayisi += cocuk_sayisi
        print(f"Çocuklarınız adına {cocuk_sayisi} adet ağaç dikilmiştir! 👍")
        break

    for cocuk in range(cocuk_sayisi):
        print("Çocuğunuz adına 1 adet ağaç dikilmiştir 🧑🏼")

print(f"Toplam Dikilen Ağaç Sayısı: {toplam_dikilen_agac_sayisi}  🎄 ")
