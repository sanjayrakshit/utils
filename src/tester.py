import src.decorators as decor


def boolify(x):
    return bool(x)

def not_not(x):
    return not not x

@decor.timeit()
def run_iter(func, args, iter):
    print(f"Doing for func: {func.__name__}")
    for _ in range(iter):
        func(*args)

@decor.cached
def fibonacci(x):
    if x == 1 or x == 2:
        return 1
    return fibonacci(x-1) + fibonacci(x-2)

@decor.timeit()    
def compute_fib(x):
    for i in range(1, x+1):
        print(f"Fib({i}) = {fibonacci(i)}")


if __name__ == "__main__":
    # 1st use case
    # run_iter(boolify, ("sanjay",), 100_000_000)
    # run_iter(not_not, ("sanjay",), 100_000_000) 
    
    # 2nd use case
    compute_fib(100)