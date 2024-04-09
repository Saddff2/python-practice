import multiprocessing as mp
import time
import random

def add_5_and_print(in_queue):
    while True:
        value = in_queue.get()  # Получаем значение из очереди
        if value == 'stop':  # Если получен маркер завершения, выходим из цикла
            break
        result, x, y = value  # Распаковываем кортеж
        print(f"x and y = {x}, {y}")  # Выводим значения x и y
        print(f"Processed value: {result}")  # Выводим результат на экран

def func():
    x = random.randint(10, 25)  # x принимает случайное значение от 10 до 25
    y = random.randint(30, 45)  # y принимает случайное значение от 30 до 45
    return x + 5, x, y  # Возвращаем кортеж с результатом и двумя значениями

if __name__ == '__main__':
    in_queue = mp.Queue()  # Очередь для передачи значений в процесс

    # Генерируем случайные числа и передаем их в очередь
    for _ in range(4):
        in_queue.put(func())

    # Запускаем процесс
    p = mp.Process(target=add_5_and_print, args=(in_queue,))
    p.start()

    # Посылаем маркер для завершения работы процесса
    in_queue.put('stop')
    p.join()
