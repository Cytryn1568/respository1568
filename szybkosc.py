import time

def silnia(n):
    if n>1:
        return n * silnia(n-1)
    else:
        return 1
    
def silnia2(n):
    wynik = 1
    for x in range(1,n+1):
        wynik *= x
    return wynik

def zmierz(f):
    t_0 = time.time()
    for x in range(10,100,10):
        w = f(x)
    t_1 = time.time()
    return t_1 - t_0

def fib(n):
    if n>2:
        return fib(n-1) + fib(n-2)
    else:
        return 1
    

    
print(zmierz(silnia))