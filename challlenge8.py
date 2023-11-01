# Assume you want to build two functions for discounting products on a website.
# Function number 1 is for student discount which discounts the current price to 10%.
# Function number 2 is for additional discount for regular buyers
# which discounts an additional 5% on the current student discounted price.
# Depending on the situation, we want to be able to apply both the discounts on the products.
# Design the above two mentioned functions and apply them both simultaneously on the price.

def students_discount(price):
    student_discount_price = price*0.90  # 10% discount for students.
    return student_discount_price

def regular_buyer_discount(price):
    regular_discount_price = price*0.95  # 5% discount for regular buyers.
    return regular_discount_price

real_price = float(input("Enter the real price of the product :"))
s_discount = students_discount(real_price)
b_discount = regular_buyer_discount(s_discount)
print("Original price :", real_price)
print("Students discount price(10%) :", s_discount)
print("Regular buyer discount price(5%) :", b_discount)
