# Written by: Valink, on: 28.11.2017

from func import *

print(
"""Prime Factorizer by Valink
Made with: Python3
      """)

act=toFactor=int(input("Enter num to factor: ")) # Act will vary through by being divided by primes

notDone=True
factors=[]

while notDone:
    notDone=False
    for n in range(2, int(act)):
        notDone=True
        if (isPrime(act)):
            factors.append(act)
            notDone = False; break

        if isPrime(n) and act%n == 0:
            act//=n
            factors.append(n)
print(factors)