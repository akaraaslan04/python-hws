string = input("Metin girin: ")
upper = 0
lower = 0

for c in string:
    if c.isupper():
        upper += 1
    elif c.islower():
        lower += 1

print("Büyük harf sayısı:", upper)
print("Küçük harf sayısı:", lower)