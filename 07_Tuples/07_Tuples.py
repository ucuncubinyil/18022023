#### Tuple: Sabit Liste ###
# Listelerden farkı değiştirilemez !

"""
sabit_liste = ()  # 1. yöntem boş tuple
sabit_liste_2 = tuple()  # 2. yöntem tavsiye edilen
"""

tercihler = (1, 2, 3, 4, "Mehmet", 25.6, False, [1, 2, 3])

print(tercihler)

for tercih in tercihler:
    print(tercih)

print(tercihler[2])
print(tercihler.index("Mehmet"))
print(tercihler.count(2))
print(len(tercihler))
print(tercihler[7][2])
