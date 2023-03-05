# Döngüler For While
# Döngüler tekrarlanan işlemleri yapan yapılardır.
"""
print(1)
print(2)
print(3)
print(4)
print(5)
"""

"""
while (kosul):
    yapılacak işlem
"""
"""
i = 1

while i <= 10:
    print(i)
    i += 1
"""
# Soru 1-100 arasındaki tek sayıları yazdırın

# i = 0
"""
while i < 101:
    if i % 2 != 0:
        print(i)
    i += 1
"""
"""
# Break => Döngüyü kırar
# Continue => Döngüyü başa atar
while i < 101:
    if i == 3:
        print(i)
        break
    i += 1
"""
"""

while True:  # Ben döngüyü kırana kadar çalış
    ad: str = input("Adınız")
    print(ad)
    if ad == "Mehmet":
        break
"""

"""
# 1-1000 arasındaki tek ve çift sayıların toplamlarını ayrı
# ayrı hesaplayan kodu yazınız if else ve while kullanın sadece
"""
"""
i: int = 0
tek_toplam: int = 0
cift_toplam: int = 0

while i <= 1000:

    if i % 2 == 0:
        cift_toplam += i
    else:
        tek_toplam += i

    i += 1

print(f"Tek Sayıların Toplamı: {tek_toplam}")
print(f"Çift Sayıların Toplamı: {cift_toplam}")
"""
"""
# kullanıcıdan alınan sayıdan-1000 arasındaki tek ve çift sayıların toplamlarını ayrı
# ayrı hesaplayan kodu yazınız if else ve while kullanın sadece
"""
"""
kullanici: int = int(input("Lütfen 0 dan farklı bir değer giriniz :"))
tek_toplam: int = 0
cift_toplam: int = 0

if kullanici < 0 or kullanici > 1000:
    print("Gireceğiniz sayı  0-1000 aralığında olmalıdır")
else:
    while kullanici <= 1000:
        if kullanici % 2 == 0:
            cift_toplam += kullanici
        else:
            tek_toplam += kullanici

        kullanici += 1

print(f"Tek Sayıların Toplamı: {tek_toplam}")
print(f"Çift Sayıların Toplamı: {cift_toplam}")
"""

"""
# 70 ile 55 arasındaki sayılarda 3'e tam bölünenleri ekrana yazdırınız
"""
"""
sayi: int = 70

while sayi >= 55:
    if sayi % 3 == 0:
        print(sayi)

    sayi -= 1

sayi: int = 55
while sayi <= 70:
    if sayi % 3 == 0:
        print(sayi)

    sayi += 1
"""
# 1'den kullanıcının girdiği sayıya kadar
# olan sayıların karesini ekrana yazdıran program.
"""
baslangic: int = 1
bitis: int = int(input("Bitiş: "))

if bitis < 1:
    print("Sayı 0 dan büyük olmalıdır")
else:
    while baslangic <= bitis:
        print(baslangic ** 2)
        baslangic += 1
"""

# Ödev: 1'den kullanıcının girdiği sayıya kadar
# olan sayıların eğer tek ise karesini , çift ise küpünün
# toplamını ayrı ayrı hesaplayan kod parçacığı


# SORU: Klavyeden girilen deger 'çık' ise döngüden
# çıkılacak. değilse toplama işlemi gerçekleştirilecek.
"""
toplam = 0
while True:
    cevap = input("Lütfen bi değer girin veya çıkmak için çık yazın").upper()

    if cevap == "ÇIK":
        break
    else:
        toplam += int(cevap)

print(toplam)
"""
# SORU: 1-100 arasındaki sayıların toplayan program.
# Ancak aşağıdak durumlarda sayıyı toplama eklemeyecek
# * Sayı 7'nin katı ise toplama eklenmesin
# * Sayı'nın 3 katının 7 fazlası 37'nın katı ise döngüden çıkılsın.

"""
sayi: int = 1
toplam: int = 0

while sayi <= 100:

    if sayi % 7 == 0:
        sayi += 1
        continue
    kat = (sayi * 3) + 7

    if kat % 37 == 0:
        print(f"Kat: {kat}")
        break
    toplam += sayi
    sayi += 1

print(toplam)
"""

# SORU: Klavyeden girilen sayının faktöriyelini hesaplayan program
# Faktoriyel => 5! => 1*2*3*4*5=120

"""
sayi: int = int(input("Faktöryeli alınacak sayıyı giriniz: "))
sayac: int = 1
sonuc: int = 1

while sayac <= sayi:
    sonuc *= sayac
    sayac += 1
    print(f" {sonuc}")

print(f"{sayi} ! = {sonuc}")
"""

# SORU:
"""
    Kullanıcıadı/Email ve şifre ile giriş sağlanacak. 3 defa giriş hakkı vardır.
        Giriş Başarılı ise ekrana "Giriş Başarılı" yazsın
        Değilse
            Kullanıcıya kayıt olmak ister misiniz?
                Hayır ise PEKİ!!!
                Evet Kullanıcıadı, ad, soyad,email,şifre ve şifre tekrarı
                alarak kayıt yapalım.
                    şifre ve şifretekrarın aynı olması
"""
"""

kullanici_adi: str = "mehmetnuri"
email: str = "info@mehmetnuri.net"
sifre: str = "123456"
hak = 3
giris_basarili: bool = False

while True:

    print("########################KULLANICI GİRİŞ PANALİ########################")

    while hak > 0:
        user_name = input("Kullanıcı adı veya email adresinizi giriniz: ")
        password = input("Şifreniz: ")

        hak -= 1

        if (kullanici_adi == user_name or email == user_name) and (sifre == password):
            print("Giriş Başarılı")
            giris_basarili = True
            break
        else:
            print("Lütfen bilgilerinizi kontrol ediniz")
            # cevap = input("Kayıt olmak ister misiniz?(E/H)").upper()
            #
            # if cevap == "E":
            #     print("Kullanıcı bilgilerini al")
            # elif cevap == "H":
            #     print("PEKİ")
            #     break
            continue

    if hak == 0:
        print("Giriş hakkınız bitti")
        break

    if giris_basarili\
            : # Değer True ise
        print("Hoş geldiniz !")
        break
"""

# SORU: Kullanıcıdan alınan sayının asal olup olmadığını ekran yazdırınız.
# Asal sayı 1 ve kendisinden başka hiç bir sayıya bölünmeyen sayıdır. 13

i: int = 2
s: int = int(input("Asallığı kontrol edilecek sayıyı giriniz: "))
asal_mi: bool = True

while i < s:

    if s % i == 0:
        asal_mi = False
        break
    i += 1
if asal_mi:
    print(f"Sayı asaldır: {s}")
else:
    print(f"Sayı asal değildir: {s}")
