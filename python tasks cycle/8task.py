from statistics import mean
a = int(input("Начало отрезка: "))
b = int(input("Конец отрезка: "))
arr = []
numbers = []
for num in range(a, b + 1):
    if num % 3 == 0:
        numbers.append(num)

print("Числа из отрезка, которые делятся на 3:")
for num in numbers:
    print(num)

if numbers: 
    average = mean(numbers)
    print(f"Среднее арифметическое этих чисел: {average}")
else:
    print("В отрезке нет чисел, кратных 3.")