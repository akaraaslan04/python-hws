choice = input("For veya While döngüsü seçiniz: ").strip().lower()

numbers = [1, 2, 3, 4, 5]
if choice == "for":
    print("For loop çıktısı:")
    for num in numbers:
        print(num)

elif choice == "while":
    print("While loop çıktısı:")
    i = 0
    while i < len(numbers):
        print(numbers[i])
        i += 1
else:
    print("Geçersiz döngü seçildi, lütfen For veya While seçiniz!")