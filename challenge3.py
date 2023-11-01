# Create a function and calculated using the formula:
# Final Price(FP) = (Product Price of X )/(Product Price of Y)^2.


def final_price(product_price_of_x, product_price_of_y):
    fp = product_price_of_x / product_price_of_y ** 2
    return fp


a = int(input("Enter the Product Price of X : "))
b = int(input("Enter the  Product Price of Y : "))
print("The Final Price (FP) =", (final_price(a, b)))
