def prime_sieve(limit): #executes a prime sieve
    #initialise the result array
    sieve = []
    for i in range(0,limit+1):
        sieve.append(0)
    #begin sieve
    i = 2
    while i < limit:
        if sieve[i] == 1:
            i += 1
            i = 2
        n = 0
        while n < limit - i:
            n += i
            sieve[n] = 1
        


prime_sieve(10)
