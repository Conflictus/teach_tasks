from statistics import mean
arr = []  
for i in range (1, 13):
    arr.append(int(input(f"Введите зарплату сотрудника: ")))

print(f"Средняя зарплата за год: {mean(arr)}")