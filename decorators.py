from datetime import datetime

def exec_time(func):
    def wrapper():
        initial_time = datetime.now()
        func()
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasron "+ str(time_elapsed.total_seconds()) + " segundos")
    return wrapper

@exec_time
def random_func():
    for _ in range(1, 10000000):
        pass

if __name__=='__main__':
    random_func()
