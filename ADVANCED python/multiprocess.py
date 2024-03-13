import multiprocessing as MP

def func(val):
    cp = MP.current_process()
    print(f'in child process name={cp.name}, pid={cp.pid}, val = {val}')

if __name__ == '__main__':
    cp = MP.current_process()
    p = MP.Process(target=func, args=('parms_val',))
    p1 = MP.Process(target=func, args=('parms_valm',))
    print(f'in main process name ={cp.name}')

    p.start()
    p1.start()
