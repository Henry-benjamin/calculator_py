price = float(input("how much is this item: "))
quantity = int(input("how manu are there: "))

total = price * quantity

print(f"{quantity} items at {price:.2f} each is : {total:.2f}")