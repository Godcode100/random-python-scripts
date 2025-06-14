from concurrent.futures import ThreadPoolExecutor
import threading

def task(n):
    print("Starting Threading Exceution:")
    print("Accessing Thread {}".format(n))
    print("{}".format(threading.get_ident()))
    print("Current Thread {}".format(threading.current_thread()))

def main():
    mythreads = ThreadPoolExecutor(max_workers=3)
    th1 = mythreads.submit(task,(4))
    th2 = mythreads.submit(task,(5))
    th3 = mythreads.submit(task,(6))

if __name__=='__main__':
    main()