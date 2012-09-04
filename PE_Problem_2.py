from functions import fib

fib_numb_roof = 4000000
fib_list = fib(fib_numb_roof)
fib_sum = 0


x = 0
y = len(fib_list)

for x in fib_list:
    if fib_list[x]%2 == 0:
        fib_sum += fib_list[x]

print fib_sum
