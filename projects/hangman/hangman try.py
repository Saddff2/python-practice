"""

1 Создать текстовый документ с перечислением слов которые будут рандомно выбираться и проверяется сколько в нем букв+
2. в зависимости от количества букв это выводится на экран
3. постройка виселицы независимая состоящая из головы тела рук и ног дается 6 попыток
4. дорисовка частей тела в зависимости от количества ошибок
5. 
"""

import random, sys


def main():
    guesses = 0
    guess_word = random_word_pick()
    print(guess_word)
    print('''Добро пожаловать в игру "Виселица"
    В этой игре вам предстоить угадать одно из слов записанных в компьютере
    НАЧИНАЕМ ИГРУ
              ''')
    print('Загаданное слово состоит из ' + str(len(guess_word)-1) + ' букв')
    hidden_word = show_hidden_word(guess_word)
    while True:
        if guesses > 6:
            print("Ты проиграл, загаданное слово было " + guess_word)
            sys.exit
        guess_letter = input('Угадай букву: ').lower()
        if guess_letter not in (guess_word):
            guesses += 1
            guess_count(guesses)
            print("Неправильно, у тебя еще " + str(6 - guesses) + " попыток")
        if guess_letter in guess_word:
            for guess_letter in enumerate(list(guess_word)):
                print(f'Ты угадал {guess_word.count(guess_letter)} букв')
                hidden_word.pop(index)
                print(hidden_word)
                    
            #else:   
            #    x = guess_word.index(guess_letter)
            #    print('Ты угадал букву')
            #    hidden_word.pop(x)
            #    hidden_word[x] = guess_letter
            #    print('Сейчас слово выглядит так: ' + str(hidden_word))
        
            

#def hidden_word_print(hidden_word):
#    for 
#

def show_hidden_word(guess_word):
    hidden_word = []
    for x in guess_word:
        hidden_word += 'x'
    return hidden_word





def random_word_pick():
    with open('c:/коды/python/projects/hangman/words.txt', 'r', encoding='utf-8') as file:
        lines = 0
        for line in file:
            lines += 1
        word_number = random.randint(1, lines)
    with open('c:/коды/python/projects/hangman/words.txt', 'r', encoding='utf-8') as file:
        for i in range(word_number - 1):
            file.readline()
        word = file.readline()
    return word.lower()


def guess_count(guesses):
    if guesses == 0:
        print("""
      _______
     |/      |
     |      
     |      
     |       
     |      
     |
 jgs_|___
""")
    elif guesses == 1:
        print("""
      _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
 jgs_|___
""")
    elif guesses == 2:
        print("""
      _______
     |/      |
     |      (_)
     |       |
     |       |
     |      
     |      
     |
 jgs_|___
""")
    elif guesses == 3:
        print("""
      _______
     |/      |
     |      (_)
     |      \|
     |       |
     |      
     |
 jgs_|___
""")
    elif guesses == 4:
        print("""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
 jgs_|___
""")
    elif guesses == 5:
        print("""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
 jgs_|___
""")
    elif guesses == 6:
        print("""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
 jgs_|___
""")





if __name__ == '__main__':
    main()