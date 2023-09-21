import time
import logging


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
