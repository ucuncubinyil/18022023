import random as rd  # random kütüphenesi içindeki her şeyi import et

# from random import random  # random kütüphenesi içindeki  random import et

print(rd.random())  # 0-1 arasında rastgele bir sayı veriyor
print(rd.randint(0, 100))  # 0-100 arasında rastgele tam sayı üret
print(rd.uniform(0, 100))  # 0-100 arasında rastgele float sayı üret
print(rd.randrange(0, 101))  # 0-100 arasında rastgele tam sayı üretir başlangıç ve bitiş sayıları dahil edilmez
print(rd.randrange(1, 100, 3))  # 0-100 arasında rastgele tam sayı üretir. 3 e bölümünden kalanı 1 olanları verir
