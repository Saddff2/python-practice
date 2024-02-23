import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'Разумеется'
    elif answerNumber == 2:
        return 'Должно быть так'
    elif answerNumber == 3:
        return 'Да'
    elif answerNumber == 4:
        return 'Попробуй еще'
    elif answerNumber == 5:
        return 'Спроси позже'
    elif answerNumber == 6:
        return 'Скоцентрируйся и спроси еще раз'
    elif answerNumber == 7:
        return 'Мой ответ нет'
    elif answerNumber == 8:
        return 'Мне кажется не очень'
    elif answerNumber == 9:
        return 'Сомневаюсь'
print("Задайте вопрос")
userInput = input()
r = random.randint(1, 9)
fortune = getAnswer(r)
print("Шар говорит: " + fortune)