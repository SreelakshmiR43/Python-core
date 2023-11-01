# Create a new list from existing list (Use String Format)
li = [30, 28, 99, 34, 10, 37, 29, 45]
new_li = "New list is {0}, {1}, {2}, {3}, {4}".format(li[6],li[2],li[7],li[1],li[5])
print(new_li)

# Create a List with 8 elements,1. Print second index to sixth index.
num = [10,20,30,40,50,60,70,80,90]
print("second index to sixth index is",num[2:7])

# .Create a tuple with 7 elements# 1. Use Insert, Append.# 2. Print the last second element.
t = ("milk","bread","egg","cheese","tea","jam","butter")
x=list(t)
x.insert(2,"coffee")
x.append("sugar")
t=tuple(x)
print("tuple :",t)
print("the last second element is:",t[-2])

