##################### AKIŞ KONTROL : IF ELIF ELSE ########################################
# Program akışında bir sonuc,durum ve değere göre program akışı
# devam edecek ise if elif else deyimleri kullanılır.
# Karar yapıların if ve else 1 kez tanımlanır.
# alternatif bütün durumlar elif keyword'ü tekrar tekrar
# yazılarak kullanılablir

"""
if koşul:
	yapılmak istenilen
else:
	eğer koşul doğru değil ise

Eşitlik Kontrolü            ==
Eşit değil kontrolü         !=
Büyüklük kontrolü           >
Küçüklük kontrolü           <
Büyük veya eşit kontrolü    >=
Küçük veya eşit kontrolü    <=
"""
# a = 1
#
# a = 5
#
# if a == 1:
#     print("Sayı 1 e eşittir")
# elif a  == 5:
#     print("Sayı 5 e eşittir")
# else:
#     print("Sayi 1 e eşit değildir ")


# 1-7 arası sayı girilsin
# hangi gün sayısı ise günün adını versin örn 5 cuma

# gun_sayisi: int = int(input("Lütfen 1-7 arasında bir sayı giriniz: "))
#
# if gun_sayisi > 7:
#     print("Girmiş oldunuz sayı 7 den büyük olamaz")
# elif gun_sayisi == 1:
#     print("Pazartesi")
# elif gun_sayisi == 2:
#     print("Salı")
# elif gun_sayisi == 3:
#     print("Çarşamba")
# elif gun_sayisi == 4:
#     print("Perşembe")
# elif gun_sayisi == 5:
#     print("Cuma")
# elif gun_sayisi == 6:
#     print("Cumartesi")
# elif gun_sayisi == 7:
#     print("Pazar")

# Ödev :
#  Kullanıcıdan 1-7 arası sayı alın.
# Bu alınan sayıyı islami gün isimlerine göre ekrana yazın
#  Örn: 1. gün  Yevmu’l-İs̠neyn
#  Pazar: Yevmu’l-Eḥad
# Pazartesi: Yevmu’l-İs̠neyn
# Salı: Yevmu’s̠-S̠ülās̠ā’
# Link: https://tr.wikipedia.org/wiki/Hicr%C3%AE_takvim


# Ödev :
#  Kullanıcıdan 1-12 arası sayı alın.
# Alınan sayıya göre ayları islami isimlerini yazdırın
# Link: https://tr.wikipedia.org/wiki/Hicr%C3%AE_takvim


# VE VEYA ( and ve or)

#
# gun_sayisi: int = int(input("Lütfen 1-7 arasında bir sayı giriniz: "))
#
# if (gun_sayisi > 7) or (gun_sayisi < 1):
#     print("Girmiş oldunuz sayı 7 den büyük veya 1 den küçük olamaz")
# elif gun_sayisi == 1:
#
#     print("Pazartesi")
# elif gun_sayisi == 2:
#     print("Salı")
# elif gun_sayisi == 3:
#     print("Çarşamba")
# elif gun_sayisi == 4:
#     print("Perşembe")
# elif gun_sayisi == 5:
#     print("Cuma")
# elif gun_sayisi == 6:
#     print("Cumartesi")
# elif gun_sayisi == 7:
#     print("Pazar")

# Aritmetiksel İşlemler
# 4 işlem

# Toplama   =>       +
# Çıkarma   =>       -
# Çarpma    =>       *
# Bölme     =>      /
# Mod Alma  =>      %
# Tam Bölme =>      //

# a = 6
# b = 9
#
# toplama = a + b
# cikarma = a - b
# carpma = a * b
# bolme = a / b
# kalan = a % b
# tam_bolme = a // b
#
# print(toplama)
# print(cikarma)
# print(carpma)
# print(bolme)
# print(kalan)
# print(tam_bolme)

# Kullanıcıdan 1 sayı alın tek mi çift mi olduğunu ekrana yazın

# sayi: int = int(input("Kontrol edilecek sayıyı girin: "))
#
# if sayi % 2 == 0:
#     print("Sayı çifttir")
# else:
#     print("Sayı tektir")


# SORU: Klavyeden girilen değer: 100'den büyükse karesini,
# küçükse küpünü ekrana yazdıran prog. ( ** üs almak için kullanılır)

# sayi: int = int(input("Kontrol edilecek sayıyı girin: "))
#
# if sayi > 100:
#     print(sayi ** 2)
# elif sayi < 100:
#     print(sayi ** 3)
# else:
#     print("Sayı 100'e eşittir")


# Kullanıcıdan alınan sayının aralığını belirleyiniz
#  0-10  11-20
# sayi: int = int(input("Kontrol edilecek sayıyı girin: "))
#
# if 0 < sayi and sayi < 11:
#     print("Sayi 0-10 aralığındadır")
# elif 10 < sayi and sayi < 21:
#     print("Sayi 10-20 aralığındadır")

# Aritmetiksel atama operatörleri
# sayi  =  sayi +1  => sayi += 1
# sayi  = sayi -1  => sayi -= 1
# ....vb  tüm aritmetiksel operatörler kullanılabilir

# a = 1
#
# a += 1  # a = a +1
#
# print(a)

# Klavyeden girilen 4 sayıdan tek ve çift olanları ayrı
# ayrı toplayarak ekrana yazdırınız..

# tek_toplam = 0
# cift_toplam = 0
#
# s1 = int(input("1. sayı"))
#
# if s1 % 2 == 0:
#     cift_toplam += s1
# else:
#     tek_toplam += s1
#
# s2 = int(input("2. sayı"))
# if s2 % 2 == 0:
#     cift_toplam += s2
# else:
#     tek_toplam += s2
#
# s3 = int(input("3. sayı"))
#
# if s3 % 2 == 0:
#     cift_toplam += s3
# else:
#     tek_toplam += s3
#
# s4 = int(input("4. sayı"))
#
# if s4 % 2 == 0:
#     cift_toplam += s4
# else:
#     tek_toplam += s4
#
# print(cift_toplam)
# print(tek_toplam)
"""
ÖDEV:  Kullanıcıdan vize final not girilmesi istensin
not aralığı 0 ile 100 arasında olmalıdır.
# vize ve finalin ortalaması alınsın.
# 0-44 : Kaldınız
# 45-69: Geçtiniz
# 70-84: İyi
# 85-100: Pekiyi
"""

# Kullanıcıdan isim,yaş,maaşve çocuk sayısı alalım

"""
    Eğer kullanıcının yaşı 45'in altındaysa;
        çocuk sayısına bakılacak ve çocuk sayısı 3^ten az ise çocuk başına 250₺,
         değilse çocuk başına 200₺ maaşa eklenecek
    Eğer kullanıcının yaşı 45 ve üzerinde ise:
        çocuk başına para verilmeyecek direk 500₺ maaşa eklenecek.
    Ekrana "Nesrin Yılmaz Maaşınız: 4000₺" yazılacak.
"""

# isim: str = input("Adınız: ")
# yas: int = int(input("Yaşınız: "))
# maas: float = float(input("Maaşınız: "))
# cocuk_sayisi: int = int(input("Çocuk sayınız: "))
#
# if yas < 45 and yas > 18:
#
#     if cocuk_sayisi < 3 and cocuk_sayisi >= 0:
#         maas += cocuk_sayisi * 250
#     else:
#         maas += cocuk_sayisi * 200
# elif yas >= 45:
#     maas += 500
#
# else:
#     print("Belirtilen yaş aralığında değilsiniz.")
#
# print(f"{isim} Maaşınız: {maas}")
# # print("{} Maaşınız: {}".format(isim,maas))


"""
ÖDEV:  Kullanıcıdan vize final not girilmesi istensin
not aralığı 0 ile 100 arasında olmalıdır.
# vize ve finalin ortalaması alınsın.
# 0-44 : Kaldınız
# 45-69: Geçtiniz
# 70-84: İyi
# 85-100: Pekiyi
"""
"""
vize_not: float = float(input("Lütfen vize notunuzu 0-100 aralığında giriniz: "))
final_not: float = float(input("Lütfen final notunuzu 0-100 aralığında giriniz: "))

if (0 <= vize_not <= 100) and (0 <= final_not <= 100):
    # Ortalama  vize %40 + final %60

    ortalama: float = (vize_not * 0.4) + (final_not * 0.6)
    print(ortalama)

    if 0 <= ortalama < 45:
        # print("Ortalamanız: {} ! Dersten kaldınız !!!".format(ortalama))
        print(f"Ortalamanız: {ortalama} ! Dersten kaldınız !!!")
    elif 45 <= ortalama < 70:
        print(f"Ortalamanız: {ortalama} ! Dersten geçtiniz !!!")
    elif 70 <= ortalama < 85:
        print(f"Ortalamanız: {ortalama} ! Dersten geçtiniz(İyi) !!!")
    else:
        print(f"Ortalamanız: {ortalama} ! Dersten geçtiniz(Pekiyi) !!!")

else:
    print("Vize ve Final notlarınız 0-100 aralığında olmalıdır")
"""

# Kullanıcı Gİriş Paneli Tasarlayınız.

"""
    Kullanıcıadı/Email ve şifre ile giriş sağlanacak
        Giriş Başarılı ise ekrana "Giriş Başarılı" yazsın
        Değilse
            Kullanıcıya kayıt olmak ister misiniz?
                Hayır ise PEKİ!!!
                Evet Kullanıcıadı, ad, soyad,email,şifre ve şifre tekrarı alarak kayıt yapalım.
                    şifre ve şifretekrarın aynı olması
"""

# kullanici_adi = "mehmetnuri"
# email = "info@mehmetnuri.net"
# sifre = "1234"
#
# print("----------------------------GİRİŞ PANELİ----------------------------")
#
# user_name_or_email: str = input("Lütfen kullanıcı adınızı veya email adresinizi giriniz: ")
# password: str = input("Lütfen şirenizi giriniz: ")
#
# if (kullanici_adi == user_name_or_email or email == user_name_or_email) and (sifre == password):
#     print("Giriş başarılı")
# else:
#     cevap: str = input("Kayıt olmak istermisiniz(E/H):").upper() # -> e -> E, a-> A
#
#     if cevap == "E":
#         ad = input("Adınız:")
#         soyad = input("Soyadınız: ")
#         username = input("Kullanıcı Adınız: ")
#         email_user = input("EMail Adresiniz: ")
#         password_user = input("Şifreniz: ")
#         password_user_control = input("Şifreniz Tekrar: ")
#
#         if password_user == password_user_control:
#             print("Hoş geldiniz !")
#             print(f"Ad: {ad}, Soyad: {soyad}, Kullanıcı Adı: {username}, E-Mail: {email_user}, Şifre: {password_user}")
#         else:
#             print("Şifreler birbirini tutmuyor")
#     elif cevap == "H":
#         print("Peki !!!")
#
#     else:
#         print("Yanlış seçim")


# Girilen 3 sayıyı büyüklük olarak karşılaştıran python uygulamasını yapınız.


"""
a b c

a > b  ve  a > c  => a
b> a  ve  b>c  => b
c 
"""
a: int = int(input("1. sayı: "))
b: int = int(input("2. sayı: "))
c: int = int(input("3. sayı: "))

if a > b and a > c:
    print(f"En büyük sayı  {a}")
elif b > a and b > c:
    print(f"En büyük sayı  {b}")
else:
    print(f"En büyük sayı  {c}")
