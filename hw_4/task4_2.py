import math
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def partial_sum(f, start, end, a, step):
    acc = 0
    for i in range(start, end):
        acc += f(a + i * step) * step
    return acc


def integrate_with_threads(f, a, b, *, n_jobs=1, n_iter=10000000):
    result = 0
    step = (b - a) / n_iter
    with ThreadPoolExecutor(max_workers=n_jobs) as executor:
        chunksize = n_iter // n_jobs
        futures = []
        for j in range(n_jobs):
            start = j * chunksize
            end = min((j + 1) * chunksize, n_iter)
            future = executor.submit(partial_sum, f, start, end, a, step)
            futures.append(future)
            print(f"starting {j} thread task 'partial_sum()' on [{start}, {end}]")
    

    for future in futures:
        result += future.result()
    return result



def integrate_with_processes(f, a, b, *, n_jobs=1, n_iter=10000000):
    result = 0
    step = (b - a) / n_iter
    with ProcessPoolExecutor(max_workers=n_jobs) as executor:
        chunksize = n_iter // n_jobs
        futures = []
        for j in range(n_jobs):
            start = j * chunksize
            end = min((j + 1) * chunksize, n_iter)
            future = executor.submit(partial_sum, f, start, end, a, step)
            futures.append(future)
            print(f"starting {j} process task 'partial_sum()' on [{start}, {end}]")
    

    for future in futures:
        result += future.result()
    return result


if __name__ == '__main__':
    for jobs_cnt in range(1, 5):
        integrate_with_threads_start = time.time()
        result = integrate_with_threads(math.cos, 0, math.pi / 2, n_jobs=jobs_cnt)
        integrate_with_threads_time = time.time() - integrate_with_threads_start
        print(f"integrate_with_threads time (n_jobs={jobs_cnt}): {integrate_with_threads_time}, result = {result}")
        print("_"*30)


        integrate_with_processes_start = time.time()
        result = integrate_with_processes(math.cos, 0, math.pi / 2, n_jobs=jobs_cnt)
        integrate_with_processes_time = time.time() - integrate_with_processes_start
        print(f"integrate_with_processes time (n_jobs={jobs_cnt}): {integrate_with_processes_time}, result = {result}")
        print("_"*30)