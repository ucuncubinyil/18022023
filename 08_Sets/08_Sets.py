### Set : Kume ###
# Tekrar eden veriler bulunmaz
# Matematikteki Kümeler kuralları geçerlidir

kume = set()  # tavsiye edilen
kume2 = {}  # tavsiye edilmeyen

# Önemli Not !!!
# set ile dolu küme oluşturulamaz (Performans)

# Kümeye Eleman Ekleme

kume.add("A")
kume.add("B")
kume.add("C")
print(kume)

kume.add(25)
kume.add(2.5)
kume.add(False)
print(kume)

print(len(kume))

# Eleman Silme

kume.remove("C") # İçerde silinecek eleman varsa siler yoksa hata verir
print(kume)

kume.discard("F") # İçerde varsa siler yoksa hata vermez
print(kume)

kume.add("A")
print(kume)
