import time
from threading import Thread
from multiprocessing import Process



def fib(n: int) -> int:
    f = [0 for _ in range(n+1)]
    if n >= 1:
        f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    print(f"calculated fib({n})")
    return f[n]


if __name__ == '__main__':
    print("sync fibonacci calc...")
    print("_"*30)
    sync_fib_start = time.time()
    for j in range(1, 11):
        fib(100000)
        print(f"{j}. iteration of sync fib(100000) completed")
    sync_fib_time = time.time() - sync_fib_start
    print("_"*30)
    print(f"sync fibonacci time: {sync_fib_time}")


    print("fibonacci calc with threading...")
    print("_"*30)
    threading_fib_start = time.time()
    fib_threads = []
    for j in range(1, 11):
        t = Thread(target=fib, args=(100000, ))
        fib_threads.append(t)
        # fib(100000)
        t.start()
        print(f"starting {j} (ident = {t.ident}) thread with fib(100000) calc")
    for idx in range(len(fib_threads)):
        t = fib_threads[idx]
        if t.is_alive():
            t.join()
        print(f"finishing {idx+1} (ident = {t.ident}) thread with fib(100000) calc")
    threading_fib_time = time.time() - threading_fib_start
    print("_"*30)
    print(f"threading fibonacci time: {threading_fib_time}")


    print("fibonacci calc with multiprocessing...")
    print("_"*30)
    multiprocessing_fib_start = time.time()
    fib_processes = []
    for j in range(1, 11):
        p = Process(target=fib, args=(100000, ))
        fib_processes.append(p)
        # fib(100000)
        p.start()
        print(f"starting {j} (pid = {p.pid}) process with fib(100000) calc")
    for idx in range(len(fib_processes)):
        p = fib_processes[idx]
        if p.is_alive():
            p.join()
        print(f"finishing {idx+1} (pid = {p.pid}) process with fib(100000) calc")
    multiprocessing_fib_time = time.time() - multiprocessing_fib_start
    print("_"*30)
    print(f"multiprocessing fibonacci time: {multiprocessing_fib_time}")