space = int(input("Введите площадь: "))
price = float(input("Введите стоимость в миллионах: "))
if space >= 100 and price <= 10 or space >= 80 and price <= 7:
    print("Квартира подходит")
else:
    print("Квартира не подходит")