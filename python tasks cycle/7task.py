amount = int(input("Сколько в классе учеников? "))
grades = []
for i in range(amount):
    while True:
        grade = int(input(f"Введите оценку ученика {i+1}: "))
        if grade in (3, 4, 5):
            grades.append(grade)
            break

counts = {
    5: grades.count(5),
    4: grades.count(4),
    3: grades.count(3)
}

most_common = max(counts, key=counts.get)

if most_common == 5:
    print("Сегодня больше отличников!")
elif most_common == 4:
    print("Сегодня больше хорошистов!")
else:
    print("Сегодня больше троечников!")

