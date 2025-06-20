
russian_score = None    
math_score = None  
info_score = None   
while True:
    try:
        russian_score = int(input("Введите количество баллов по русскому языку: "))
        if 0 <= russian_score <= 100:
            break
        else:
            print("Баллы должны быть в диапазоне от 0 до 100.")
    except ValueError:
        print("Ошибка: введите целое число!")
while True:
    try:
        math_score = int(input("Введите количество баллов по математике: "))
        if 0 <= math_score <= 100:
            break
        else:
            print("Баллы должны быть в диапазоне от 0 до 100.")
    except ValueError:
        print("Ошибка: введите целое число!")
while True:
    try:
        info_score = int(input("Введите количество баллов по информатике: "))
        if 0 <= info_score <= 100:
            break
        else:
            print("Баллы должны быть в диапазоне от 0 до 100.")
    except ValueError:
        print("Ошибка: введите целое число!")


total_score = russian_score + math_score + info_score
if total_score >= 270:
    print("Поздравляю, ты поступил на бюджет!")
else:
    print("К сожалению, ты не прошёл на бюджет.")