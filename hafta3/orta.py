while True:
    print("\nHesap Makinesi")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Çıkış")

    secim = input("İşlem seçin: ")

    if secim == "5":
        print("Çıkış yapılıyor...")
        break

    if secim not in ["1", "2", "3", "4"]:
        print("İşlem yapılamaz")
        continue

    try:
        a = float(input("Birinci sayıyı girin: "))
        b = float(input("İkinci sayıyı girin: "))

        if secim == "1":
            sonuc = a + b
        elif secim == "2":
            sonuc = a - b
        elif secim == "3":
            sonuc = a * b
        elif secim == "4":
            if b == 0:
                print("İşlem yapılamaz")
                continue
            sonuc = a / b

        if sonuc == int(sonuc):
            print("Sonuç:", int(sonuc))
        else:
            print("Sonuç:", sonuc)

    except ValueError:
        print("İşlem yapılamaz")