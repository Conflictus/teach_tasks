prices = [0, 0, 0]
for i in range(len(prices)):
    while True:
        try:
            price = int(input(f"Введите цену стула {i + 1}: "))
            if price >= 0:
                prices[i] = price
                break
            else:
                print("Цена не может быть отрицательной.")
        except ValueError:
            print("Пожалуйста, введите целое число.")
sum_prices = sum(prices)
if sum(prices) > 10000:
    
    sum_prices *= 0.9

print(f"Итоговая цена стульев {sum_prices}p")