arr = []  
for i in range (1, 11):
    arr.append(int(input(f"Введите номер человека:")))

a = sum(1 for i in arr if i >= 0 and i % 2 == 0)
print(f"Количество корректных номеров (чётных и положительных): {a}")