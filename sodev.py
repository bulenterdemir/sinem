def isprime(n):
    if n < 2:
        return None
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sieve(n):
    if n < 2:
        return None
    sieve = [True] * (n+1)
    for x in range(2, int(n**0.5) + 1):
        if sieve[x]:
            for i in range(x*x, n+1, x):
                sieve[i] = False
    return [i for i in range(2, n+1) if sieve[i]]
    
def factorization(n):
    if n < 2:
        return None
    if n == 2:
        return [[2, 1]]

    m = n // 2 + (n % 2)
    Kandidaten = sieve(m)
    Faktoren = []

    for Kandidat in Kandidaten:
        Anzahl = 0
        while n % Kandidat == 0:
            Anzahl += 1
            n //= Kandidat

        if Anzahl > 0:
            Faktoren.append([Kandidat, Anzahl])

    if n > 1:
        Faktoren.append([n, 1])

    return Faktoren

def euler_phi(n):
    if n < 1:
        return None
    if n == 1:
        return 1
    if isprime(n):
        pf, e = factorization(n)[0]
        EP = pf * e - pf * (e - 1)
        return EP
    else:
        F = factorization(n)
        EP = 1
        for f, e in F:
            EP = f * e - f ** (e - 1)
        return EP
    
def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def iscoprime(m, n):

    if m < 1 or n < 1:
        return None

    if m == n:
        return m == 1  

    return gcd(m, n) == 1


a=sieve(14)
print(a)