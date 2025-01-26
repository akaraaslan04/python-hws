capitals = {
    "Türkiye": "Ankara",
    "Rusya" : "Moskova",
    "Azerbaycan" : "Bakü"
}

e_list = []

for i in capitals.items():
    e_list.append(i)


for i in e_list[::-1]:
    for j in i:
        print(j)