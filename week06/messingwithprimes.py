# Generate primes
# Authoer : Michelle O'Connor


primes = []
upto = 100000

candidates = range(2, upto+1)
print (type(candidates))

for candidate in candidates:
    print(candidate, end= " ")
    isPrime = True

    # check if it is a prime
    for divisor in primes:
        if candidate % divisor == 0:
            isPrime = False
            break
    
    # if it is still a prime
    if isPrime:
        primes.append(candidate)


print (primes)


