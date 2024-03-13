import multiprocessing as mp
import threading
import time
import random

def worker(thread_num, process_num):
    pid = mp.current_process().pid
    sleep_time = random.randint(1, 5)
    print(f"Process {pid} in Thread {thread_num} started and will sleep for {sleep_time} seconds")
    time.sleep(sleep_time)
    print(f"Process {pid} in Thread {thread_num} finished")

def thread_worker(thread_num):
    for process_num in range(1, 5):
        p = mp.Process(target=worker, args=(thread_num, process_num))
        p.start()
        p.join()

if __name__ == "__main__":
    threads = []
    for thread_num in range(1, 5):
        t = threading.Thread(target=thread_worker, args=(thread_num,))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()

    print("All threads finished")
