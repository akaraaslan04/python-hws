stu = {
    "Ali": [85.0, 90.0, 78.0],
    "Zehra": [92.0, 88.0, 95.0],
    "Efe": [75.0, 80.0, 68.0]
}

while True:
    op = input("""
               Ögrenci Not Y¨onetim Sistemine Hoş Geldiniz!
                1. Ögrenci Ekle
                2. Ögrenci Sil
                3. Not Ekle
                4. Ögrenci Notlarını Görüntüle
                5. Ortalama Hesapla
                6. Geçme Durumunu Kontrol Et
                7. Sınıfın Genel Ortalamasını Hesapla
                8. En Yüksek ve En Düşük Notları Bul
                9. Cıkış
                Seçiminizi yapın (1-9): 
               """)
    if op == "9":
        break
    elif op == "1":
        name = input("Öğrenci ismi: ")
        if name in stu:
            print(f"{name} zaten mevcut ")
        else:
            stu[name] = []
            print(f"{name} eklendi")
    elif op == "2":
        name = input("Silinecek öğrenci ismi: ")
        if name in stu:
            del stu[name]
        else:
            print(f"{name} bu sınıfta mevcut değil")
    elif op == "3":
        name = input("Not eklenecek öğrenci ismi: ")
        if name in stu:
            try:
                mark = float(input("Not eklenecek öğrenci ismi: "))
                stu[name].append(mark)
                print(f"{name} isimli öğrenciye {mark} notu eklendi")
            except ValueError:
                print("Geçersiz not değeri!")
        else:
            print(f"{name} bu sınıfta mevcut değil")
        
    elif op == "4":
        name = input("Notlarını görüntülemek istediğiniz öğrencinin ismi: ")
        if name in stu:
            index = 0
            print(f"{name} isimli öğrencinin notları: ")
            for i in stu[name]:
                print(f"{stu[name][index]}")
                index +=1
        else:
            print(f"{name} bu sınıfta mevcut değil")
    elif op == "5":
        name = input("ortalama hesaplanacak öğrenci ismi: ")
        if name in stu:
            sum = 0
            index = 0
            for mark in stu[name]:
                sum += mark
                index += 1
            avg = sum / index
            print(f"{name} isimli öğrencinin ortalaması: {avg}")
            
        else:
            print(f"{name} bu sınıfta mevcut değil")
        
    elif op == "6":
        name = input("Geçme durumu kontrol edilecek öğrenci ismi: ")
        if name in stu:
            sum = 0
            index = 0
            for mark in stu[name]:
                sum += mark
                index += 1
            avg = sum / index
            if avg >= 60:
                print(f"{name} isimli öğrenci, {avg} ortalama ile geçti")  
            else:
                print(f"{name} isimli öğrenci, {avg} ortalama ile kaldı")
        else:
            print(f"{name} bu sınıfta mevcut değil")
        
    elif op == "7":
        total_sum = 0
        total_count = 0
        for marks in stu.values():
            total_sum += sum(marks)
            total_count += len(marks)
        if total_count > 0:
            class_avg = total_sum / total_count
            print(f"Sınıfın genel ortalaması: {class_avg}")
        else:
            print("Notlar yok, ortalama hesaplanamıyor")
    elif op == "8":
        highest_mark = None
        lowest_mark = None

        for marks in stu.values():
            for mark in marks:
                if highest_mark is None or mark > highest_mark:
                    highest_mark = mark
                if lowest_mark is None or mark < lowest_mark:
                    lowest_mark = mark

        if highest_mark is not None and lowest_mark is not None:
            print(f"Sınıftaki en yüksek not: {highest_mark}")
            print(f"Sınıftaki en düşük not: {lowest_mark}")
        else:
            print("Sınıfta herhangi bir not bulunmamaktadır.")
    else:
        print("Geçersiz işlem!")