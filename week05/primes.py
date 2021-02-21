# generate primes
# Author : Michelle O'Connor

primes = []

for candidate in range (2, 101):
    # print (candidate)
    isPrime = True
    for divisor in range(2,candidate):
        if (candidate % divisor == 0):
            isPrime = False
            break
            
    if isPrime:
        primes.append(candidate)


print (primes)
