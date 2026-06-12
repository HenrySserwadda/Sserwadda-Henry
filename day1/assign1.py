print("   Bill Split Calculator \n")


total_bill = float(input("Enter total bill amount: "))
num_people = int(input("Enter number of people: "))


print("Select tip percentage:")
print("1. 10%")
print("2. 15%")
print("3. 20%")
print("4. Custom")

choice = input("Enter choice (1-4): ")

if choice == "1":
    tip_percent = 10
elif choice == "2":
    tip_percent = 15
elif choice == "3":
    tip_percent = 20
elif choice == "4":
    tip_percent = float(input("Enter custom tip percentage: "))
else:
    print("Invalid choice. Defaulting to 15%.")
    tip_percent = 15


tip_amount = total_bill * (tip_percent / 100)
total_with_tip = total_bill + tip_amount
amount_per_person = total_with_tip / num_people


print(f"\n     RECEIPT    ")
print(f"Original Bill:    UGX{total_bill}")
print(f"Tip ({tip_percent}%):       UGX{tip_amount}")
print(f"Total Bill:       UGX{total_with_tip}")
print(f"Number of People: {num_people}")
print(f"-----------------------------")
print(f"Each Person Pays: UGX{amount_per_person}")
