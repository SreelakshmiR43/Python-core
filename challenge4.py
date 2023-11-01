# Write a function which would divide two numbers,
# design the function in a manner that it handles the divide by zero exception.
def divide(a,b):
    return a/b
try:
    x = float(input("1st number : "))
    y = float(input("2nd number : "))
    print(divide(x, y))
except ZeroDivisionError:
    print("There is a Division Error")
finally:
    print("Finished!!")


