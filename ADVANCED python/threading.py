import threading
import time

def numbered_operations():
    for i in range(1, 11):
        print(f"Operation {i}")
        time.sleep(0.5)

def user_interactions(number):
    for i in range(1, 6):
        result = number * i
        print(f"User: {number} - Operation {i} - Result: {result}")
        time.sleep(0.25)

def main():
    # Запуск операций с перечислением в отдельном потоке
    operations_thread = threading.Thread(target=numbered_operations)
    operations_thread.start()

    # Ожидание ввода от пользователя
    user_input = input("Введите число: ")
    number = int(user_input)

    # Запуск взаимодействий с числом в отдельном потоке
    interactions_thread = threading.Thread(target=user_interactions, args=(number,))
    interactions_thread.start()

    # Ожидание завершения обоих потоков
    operations_thread.join()
    interactions_thread.join()

if __name__ == "__main__":
    main()
