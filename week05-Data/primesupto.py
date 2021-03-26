# generate primes up to
# Author : Michelle O'Connor

primes = []
upto = 10001


for candidate in range (2, upto):
    # print (candidate)
    isPrime = True
    # only need to check if divisable by prime
    for divisor in primes:
        # if divisable by an int it is not a prime numner
        if (candidate % divisor == 0):
            isPrime = False
            # so there is not reason to keep checking
            break
            
    if isPrime:
        primes.append(candidate)


print (primes)
