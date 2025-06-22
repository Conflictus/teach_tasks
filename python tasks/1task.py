experience = int(input("Введите количество опыта: "))

if experience < 1000:
    level = 1
elif experience < 2500:
    level = 2
elif experience < 5000:
    level = 3
else:
    level = 4

print(f"Ваш уровень: {level}")