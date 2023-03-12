# SORU:
# 1-15 arasında 5'er adet sayı üretip 2 farklı kümeye kaydediniz.
# Daha Sonra iki kümeyi ekrana yazdırınız. (iki kümede ortak eleman olmasın)

from random import randint

kume1: set = set()
kume2: set = set()
for i in range(5):
    while True:
        sayi: int = randint(1, 16)
        if len(kume1) < 6:
            if sayi not in kume1 and sayi not in kume2:
                kume1.add(sayi)
                break
            else:
                continue
        else:
            continue

    while True:
        sayi: int = randint(1, 16)

        if len(kume2) < 6:
            if sayi not in kume1 and sayi not in kume2:
                kume2.add(sayi)
                break
            else:
                continue
        else:
            continue

print(kume1)
print(kume2)

kume3 = set()
kume4 = set()
while len(kume3) < 5:
    sayi = randint(1, 16)
    if sayi not in kume4 and sayi not in kume3:
        kume3.add(sayi)

while len(kume4) < 5:
    sayi = randint(1, 15)
    if sayi not in kume4 and sayi not in kume3:
        kume4.add(sayi)
print(kume3)
print(kume4)
