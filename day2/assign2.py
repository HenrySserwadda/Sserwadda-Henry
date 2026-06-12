#create ecommerce system that checks inputs like subtotal, discount, tax to calculate the final price of a product. Include the coupon code for discount and tax rate for the calculation.Use nested conditons to handle different scenarios such as valid/invalid coupon codes, different tax rates based on location and various discount levels based on the subtotal amount.Implement log
#https://github.com/drjeffgeoff/BSE_RECESS_26.git
# E-Commerce System

print("===== LOGIN SYSTEM =====")

username = input("Enter username: ")
password = input("Enter password: ")

# User database
if username == "admin" and password == "admin123":
    role = "Admin"

elif username == "customer" and password == "cust123":
    role = "Customer"

elif username == "cashier" and password == "cash123":
    role = "Cashier"

else:
    print("Invalid username or password!")
    exit()

print(f"\nWelcome {username}")
print("Role:", role)

# Access levels
if role == "Admin":
    print("Access: Full system access")

elif role == "Cashier":
    print("Access: Process sales and payments")

elif role == "Customer":
    print("Access: Purchase products")

print("\n===== E-COMMERCE CHECKOUT =====")

subtotal = float(input("Enter subtotal amount: "))

coupon = input("Enter coupon code: ")

location = input("Enter location (Uganda/Kenya/Tanzania): ")

# Discount calculation
discount = 0

if subtotal >= 1000:
    discount = subtotal * 0.20
elif subtotal >= 500:
    discount = subtotal * 0.10
else:
    discount = subtotal * 0.05

# Coupon validation
if coupon == "SAVE10":
    discount += subtotal * 0.10
    print("Valid coupon applied!")
else:
    print("Invalid coupon code!")

price_after_discount = subtotal - discount

# Tax calculation based on location
if location == "Uganda":
    tax_rate = 0.18

elif location == "Kenya":
    tax_rate = 0.16

elif location == "Tanzania":
    tax_rate = 0.15

else:
    tax_rate = 0.10
    print("Unknown location. Default tax applied.")

tax = price_after_discount * tax_rate

final_price = price_after_discount + tax

print("\n===== RECEIPT =====")
print("Subtotal:", subtotal)
print("Discount:", discount)
print("Price After Discount:", price_after_discount)
print("Tax:", tax)
print("Final Price:", final_price)

# Nested conditions example
if role == "Admin":
    if final_price > 1000:
        print("Admin approval: Large transaction detected.")
    else:
        print("Admin approval not required.")

elif role == "Cashier":
    if final_price > 500:
        print("Manager approval required.")
    else:
        print("Transaction processed.")

elif role == "Customer":
    if final_price > 200:
        print("Eligible for free delivery.")
    else:
        print("Standard delivery applies.")