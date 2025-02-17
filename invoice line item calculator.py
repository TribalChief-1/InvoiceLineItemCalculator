
#Function Calls

def item_price():
    while True:
        try:
            price = float(input("Enter the price of the item: "))
            if price < 0:
                print("Price may not be negative")
                continue
            return price
        except ValueError:
            print("Invalid numerical value. Please enter a price value.")

def item_quantity():
    while True:
        try:
            quantity = int(input("Enter the quantity: "))
            if quantity < 0:
                print("Quantity may not be negative.")
                continue
            return quantity
        except ValueError:
            print("Invalid numerical Value. Please enter a quantity")

#Calling All Functions

def main():
    print("**** Invoice Line Item Calculator ****")
    while True:
        start = input("Would you like to enter an item (y/n): ").strip().lower()

        if start == 'n':
            break
        elif start != 'y':
            print("Invalid entry. Press 'y' to continue or 'n' to exit.")
            continue

        price = item_price()
        quantity = item_quantity()
        total = price * quantity

        print("----- Invoice ----- ")
        print(f"Price: ${price:.2f}")
        print(f"Quantity: {quantity}")
        print(f"Total: ${total:.2f}")
        print("_____________________\n")

        cont = input("Would you like to enter another line item? (y/n).").strip().lower()
        if cont != 'y':
            break

if __name__ == "__main__":
    main()