def fib(n):    # write Fibonacci series up to n
    fib_numb = []
    a,b = 0,1
    while b < n:
        fib_numb.append(b)
        a, b = b, a+b
    return(fib_numb)
