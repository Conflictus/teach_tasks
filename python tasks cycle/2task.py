number = int(input("Введите число:  "))
if 0 <= number:
    to_string = str(number)
    print(f"Кол-во цифр в числе: {len(to_string)}")
else:
    print("число должно быть неотрицательным")
    quit()
