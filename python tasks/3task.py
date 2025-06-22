import datetime

date = datetime.date.today  #int(input("введите сегодняшнюю дату: "))
number = date().day
if number%2 == 0:
    print("Сегодня рабочий день")
else: 
    print("сегодня выходной")