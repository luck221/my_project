from random import randint
import threading
import time

def main():
    def action(level , result):
        t1 = time.time()
        lock.acquire()
        try:
            for i in range(level , level+m // n):
                result += work_list[i]
            level += m//n    
            print(f"Отработал {result}")                    
        finally:
            lock.release()
            t2 = time.time()  
            print(t2-t1)  

    # m - lenght of list
    m = int(input())
    # n - quantity of thread
    n = int(input())
    level = 0 
    work_list = [randint(1,10) for i in range(m)]
    print(work_list)

    result = 0 

    list_thread = []
    lock = threading.Lock()

    for i in range(n):
        thread = threading.Thread(target = action , args=(level,result))
        thread.start()

    for thread in list_thread:
        thread.join()



if __name__ == "__main__":
    main()