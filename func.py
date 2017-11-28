from time import time
def isPrime(n):
    if n%2 == 0 and not(n==2):
        return False

    for i in range(3,n,2):
        if n%i == 0:
            return False
    return True