number = int(input("задайте число: "))
count = 0
while True:
    guess = int(input("угадайте число: "))
    count += 1
    if guess > number:
        print("Число больше, чем нужно. Попробуйте ещё раз!")
    elif guess < number:
        print("Число меньше, чем нужно. Попробуйте ещё раз!")
    elif guess == number:
        print(f"Вы угадали! Число попыток: {count}")
        break