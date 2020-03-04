import time

def silnia(n):
    if n>1:
        return n * silnia(n-1)
    else:
        return 1
    
def silnia2(n):
    wynik = 1
    for n in range(1,n+1):
        wynik *= n
    return wynik

def zmierz(f,n=100):
    t_0 = time.time()
    w = f(n)
    t_1 = time.time()
    return t_1 - t_0

print(zmierz(silnia))