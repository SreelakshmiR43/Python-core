def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1) # fn calling itself
result=fact(5)
print(result)