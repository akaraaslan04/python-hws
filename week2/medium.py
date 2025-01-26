advs = {}

while True:
    
    print("""
        1-Yeni İlan Ekle
        2-İlan Çıkar
        3-Çıkış
        """)
    
    choice = input("İşlem seçiniz: ")
    
    if(choice == "1"):
        adv_name = input("Yeni ilanın adını girin: ")
        
        if adv_name in advs:
            print("Bu ilan zaten var")
            continue
        
        brand = input("Markayı girin: ")
        model = input("Modeli girin: ")
        year = input("Aracın üretim ylını girin: ")
        price = input("Aracın fiyatını girin: ")
        
        feat = {
            "Marka" : brand,
            "Model" : model,
            "Yıl" : year,
            "Fiyat" : price
        }
        
        advs[adv_name] = feat
        print(f"{adv_name} başarıyla eklendi \n {feat}")
    elif choice == "2":
        
        adv_name = input("Sileceğiniz ilanın ismini yazın: ")
        
        if(adv_name in advs):
            del advs[adv_name]
            print(f"{adv_name} silindi")
        else:
            print("Böyle bir ilan yok")

    elif choice == "3":
        print("Programdan çıkılıyor")
        break
    else:
        print("Geçersiz işlem")