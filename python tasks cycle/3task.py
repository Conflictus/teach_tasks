import math
x = int(input("Вклад в банке:  "))
p = int(input("Процент:  "))
y = int(input("Порог вклада: "))
a = x
i = 1 # year
while True:
    print(f"{i} год. {a} + {p}% = {math.floor(x)}")
    if x >= y:
        print(f"Кол-во лет для достижения порога: {i}")
        break
    a = math.floor(x)
    x += x * p / 100
    i += 1
        
       