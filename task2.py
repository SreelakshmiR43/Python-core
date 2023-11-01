def simple_interest(p,n,r):
    s =p*n*r/100
    return s


x = float(input("Enter the principal amount (p) : "))
y = float(input("Enter the period in years (n) : "))
z = float(input("Enter the rate (r) : "))
print("Simple Interest =",simple_interest(x,y,z))