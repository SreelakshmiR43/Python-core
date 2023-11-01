x=("hai","helllo",3)
print(x)
print(type(x))

# tuple is immutable,
# to change the tuple, we have to convert tuple to list and after that change the list to tuple.

# eg:

y=list(x)
print(y)
print(type(y))

y.insert(2,"number")
print(y)

x = tuple(y)
print(x)
print(type(x))