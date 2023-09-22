import time
import logging
from typing import *


def timeit(logger: logging = None):
    def timeit_inner(func: callable):
        """Decorator to print/log time taken by a function"""
        def _timeit_inner(*args, **kwargs):
            start = time.time()
            r = func(*args, **kwargs)
            end = time.time()
            if logger is None:
                print(f"Time taken for func : {func.__name__}, is : {(end-start):.7f} sec(s)")
            else:
               logger.info(f"Time taken for func : {func.__name__}, is : {(end-start):.7f} sec(s)") 
            return r
        return _timeit_inner
    return timeit_inner


def cached(func):
    cache = {}
    def cached_inner(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return cached_inner


def retryer(retry_count: int = 1, gap: int = 5):
    def retryer_inner(func):
        def _retryer_inner(*args, **kwargs):
            last_exception = None
            for i in range(retry_count):
                try:
                    r = func(*args, **kwargs)
                    return r
                except Exception as e:
                    last_exception = e
                    print(f"Exception found : {e} [in {i+1}/{retry_count} tries... waiting for {gap} sec(s)]")
                    time.sleep(gap)
            raise last_exception
        return _retryer_inner
    return retryer_inner

