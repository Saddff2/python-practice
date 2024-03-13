import multiprocessing as MP
import time

def func():
    for i in range(100000000):
        pass
    
def func1(number):
    for i in range(10,1,-1):
        print(number/i)
        time.sleep(1)
    
    
if __name__ == "__main__":
    p = MP.Process(target=func1, args=(255 ,))
    p.start()
    p.join(1)
    while p.exitcode is None:
        print("in loop")
        p.join(1)
        
    print("p.exitcode", p.exitcode)