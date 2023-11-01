# Print Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8, 13,21, 34, 55, 89, 144

def fib(x):
    if x <= 0:
        return []
    elif x==1:
        return [0]
    elif x==2:
        return [0,1]
    else:
        series = fib(x-1)
        series.append(series[-1]+series[-2])
        return series

x=13
series = fib(x)
for i in series:
    print(i,end=" ")