place = int(input("Введите место в списке поступающих: "))
if place < 0:
    print("Место не может быть отрицательным.")
    exit()
elif place <= 10:
    score = int(input("Введите балл за экзамен: "))
    if score < 0 or score > 300:
        print("Баллы должны быть в диапазоне от 0 до 300.")
        exit()
    elif score >= 270:
        print("Поздравляем, вы поступили!")
        print("Бонусом вам будет начисляться стипендия.")
    else:
        print("Поздравляем, вы поступили!")
else:
    print("К сожалению, вы не поступили.")
