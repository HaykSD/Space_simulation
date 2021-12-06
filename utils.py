# Created by Hayk_Sardaryan at 12/03/2021 / 15:32
from time import perf_counter
from functools import wraps

def calc_time(times):
    count = 1
    work_time = 0
    def wrapper(func):
        @wraps(func)
        def inner(*args,**kwargs):
            nonlocal count,work_time
            stat_time = perf_counter()
            res = func(*args,**kwargs)
            work_time+=perf_counter() - stat_time
            if not count%times:
                print(f"{func.__name__} works at {work_time} second {times} times: Round{work_time/times:.7f}")
                count =0
            count+=1
            return res

        return inner
    return wrapper


def get_screen_size(minus):
    ''':return with, height'''
    import ctypes
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    print('w =', user32.GetSystemMetrics(0) - minus, ', h =', user32.GetSystemMetrics(1) - minus)
    return user32.GetSystemMetrics(0) - minus, user32.GetSystemMetrics(1) - minus
