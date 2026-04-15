print("Welcome to Smart Shop")

total = 0
choice = 0

while choice != 5:

    print("1. Apple - 10 tk")
    print("2. Banana - 5 tk")
    print("3. Milk - 50 tk")
    print("4. Bread - 40 tk")
    print("5. Exit")

    choice = int(input("Enter Your Product Choice: "))

    if choice == 5:
        break

    if choice < 1 or choice > 5:
        print("Invalid Choice Input!")
        continue

    quantity = int(input("Enter Product Quantity: "))

    if quantity <= 0:
        print("Invalid Product Quantity.")
        continue

    if choice == 1:
        total = total + 10 * quantity
    elif choice == 2:
        total = total + 5 * quantity
    elif choice == 3:
        total = total + 50 * quantity
    elif choice == 4:
        total = total + 40 * quantity

    print("Your Total is Bill:", total, "tk")

print("Final Total Bill:", total, "tk")
print("Thank you!!")





