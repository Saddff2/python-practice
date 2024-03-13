import multiprocessing as MP
import time

def func():
    for i in range(100000000):
        pass
    
    
if __name__ == "__main__":
    p = MP.Process(target=func)
    p.start()
    p.join(1)
    while p.exitcode is None:
        print("in loop")
        p.join(1)
        
    print("p.exitcode", p.exitcode)