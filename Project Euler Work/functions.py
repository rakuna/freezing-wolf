def fib(n):    # write Fibonacci series up to n
    fib_numb = []
    a,b = 0,1
    while b < n:
        fib_numb.append(b)
        a, b = b, a+b
    return(fib_numb)


#Problem 1:
def factor_summation(factor, limit): #computes the summation of all multiples of 'factor' up to 'limit'
    i = 0
    summation = 0
    while (i + factor < limit):
        i += factor
        summation += i
    return(summation)
