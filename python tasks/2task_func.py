def define_function(x):
    if x < 0:
        y = x - 12
    elif x == 0:
        y = 5
    elif x > 0:
        y = x * 2
    return y
x = int(input("Введите X координату: "))
print(f"Y координата: {define_function(x)}")