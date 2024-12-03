import time

def meric_casu(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        konec = time.time()
        print(f"Potrebny cas: {konec - start} vterin")
        return result
    return wrapper

@meric_casu
def find_primes(a,b):
    primes = []
    for num in range(a, b+1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

primes = find_primes(8,30)
print(f"Prime numbers from 0 to 1000: {primes}")