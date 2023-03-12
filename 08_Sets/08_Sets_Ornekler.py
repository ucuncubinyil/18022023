kume = {11, 22, 33, 44}
kume2 = {33, 44, 55, 66, 77, 88, 99}
"""
# Küme Farkı Bulma

kume_fark = kume - kume2 # 1. yöntem tavsiye edilmeyen
print(kume_fark)

kume_fark_2 = kume2 - kume
print(kume_fark_2)

tavsi_edilen = kume.difference(kume2)# tavsiye edilen yöntem
print(tavsi_edilen)

tavsi_edilen2 = kume2.difference(kume)
print(tavsi_edilen2)
"""
# Küme Birleşim

kume_birlesim = kume.union(kume2)
print(kume_birlesim)

for eleman in kume_birlesim:
    print(eleman)

kume_birlesim2 = kume2.union(kume)
print(kume_birlesim2)

for eleman in kume_birlesim2:
    print(eleman)

print(kume_birlesim2)

# Var olan kümeye baska bir kümenin elemanlarını elkeyip güncellemek

turkiye = {"istanbul", "ankara", "izmir", "malatya"}
afrika = {"cibuti", "senegal", "gabon"}

turkiye.update(afrika)
print(turkiye)

turkiye.discard("gabon")
print(turkiye)

# İlk elemanı siler
turkiye.pop()
print(turkiye)

# Kümeyi temizleme
turkiye.clear()
print(turkiye)

del turkiye  # ramden siler

# Alt Küme
print(f"Küme kümesi Küme2 kümesinin alt kümesimidir? : {kume.issubset(kume2)} ")

#Üst Küme
print(f"Küme kümesi Küme2 kümesinin üst kümesimidir? : {kume.issuperset(kume2)} ")


#Ayrık Küme
print(f"Küme kümesi Küme2 kümesinin ayrık kümesimidir? : {kume.isdisjoint(kume2)} ")


