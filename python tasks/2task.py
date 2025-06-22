scores = []
subjects = ['русскому языку', 'математике', 'информатике']
while True:
    try:
        score = int(input(f"Введите балл по {subjects[len(scores)]}: "))
        if 0 <= score <= 100:
            scores.append(score)
        else:
            print("Баллы должны быть в диапазоне от 0 до 100.")
    except ValueError:
        print("Пожалуйста, введите целое число.")

    if len(scores) == 3:
        break


russian_score, math_score, info_score = scores
total_score = russian_score + math_score + info_score
if total_score >= 270:
    print("Поздравляю, ты поступил на бюджет!")
else:
    print("К сожалению, ты не прошёл на бюджет.")