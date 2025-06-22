import random
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
if num1 >= num2:
    print(num1-num2, "\nИгрок платит")
else:
    print(num2+num1, "\nВладелец платит")

print("Игра окончена")