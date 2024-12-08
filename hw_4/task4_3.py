import codecs
import multiprocessing as mp
from time import sleep
from datetime import datetime


def main_handler(a_queue, messages):
    print("starting main process")
    print("_"*30)
    for msg in messages:
        a_queue.put(msg)


def A_handler(a_queue, b_queue):
    print("starting A process")
    print("_"*30)
    while not a_queue.empty():
        print(f"a_queue size = {a_queue.qsize()}")
        b_msg = f"[{datetime.now().astimezone().isoformat()}] message = {a_queue.get().lower()}"
        b_queue.put(b_msg)
        sleep(5)
        print("sleeping for 5 sec")


def B_handler(b_queue, main_queue):
    print("starting B process")
    print("_"*30)
    while not b_queue.empty():
        msg_timestamp, msg = b_queue.get().split('=')
        enc = codecs.encode(msg, 'rot_13')
        print(f"{msg_timestamp} {enc}")
        main_queue.put(f"{msg_timestamp} {enc}")


if __name__ == '__main__':
    A_queue = mp.Queue()
    B_queue = mp.Queue()
    main_queue = mp.Queue()
    a_conn_parent, b_conn_child = mp.Pipe()
    messages = ["first", "second", "third", "fourth", "fifth"]
    main = mp.Process(target=main_handler, args=(A_queue, messages))
    A = mp.Process(target=A_handler, args=(A_queue, B_queue))
    B = mp.Process(target=B_handler, args=(B_queue, main_queue))
    main.start()
    print(f"created main process with pid = {main.pid}")
    main.join()
    A.start()
    print(f"created A process with pid = {A.pid}")
    A.join()
    B.start()
    print(f"created B process with pid = {B.pid}")
    B.join()