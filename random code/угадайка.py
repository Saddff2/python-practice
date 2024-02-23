import random

secretNumber = random.randint(1,20)
print("Я загадал число от 1 до 20")

for guess in range (1,7):
    print("Угадай число:")
    num = int(input())
    
    if num < secretNumber:
        print("Загаданое число больше")
    elif num > secretNumber:
        print('Загаданое число меньше')
    else:
        break

if num == secretNumber:
    print("красавчик угадал с " + str(guess) + " попытки")
else:
    print("лох это было " + str(secretNumber))