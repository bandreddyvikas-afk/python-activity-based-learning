
# Order and Inventory Management

products = ["Product A", "Product B", "Product C", "Product D"]
ordered = [100, 80, 60, 50]
dispatched = [70, 90, 40, 30]
returned = [5, 10, 45, -2]
inventory = [200, 150, 100, 80]

print("ORDER AND INVENTORY REPORT")
print("-" * 75)

for i in range(len(products)):
    print("\nProduct:", products[i])

    # Validate quantities
    if (ordered[i] < 0 or dispatched[i] < 0
            or returned[i] < 0):
        print("Error: Negative quantity found")
        print("Record marked inconsistent")
        continue

    if dispatched[i] > ordered[i]:
        print("Error: Dispatch exceeds ordered quantity")
        print("Record marked inconsistent")
        continue

    if returned[i] > dispatched[i]:
        print("Error: Returns exceed dispatched quantity")
        print("Record marked inconsistent")
        continue

    if inventory[i] < dispatched[i] - returned[i]:
        print("Error: Insufficient inventory")
        print("Record marked inconsistent")
        continue

    # Calculate order status and inventory
    outstanding = ordered[i] - dispatched[i]
    updated_inventory = (
        inventory[i] - dispatched[i] + returned[i]
    )

    print("Ordered quantity:", ordered[i])
    print("Dispatched quantity:", dispatched[i])
    print("Returned quantity:", returned[i])
    print("Outstanding order:", outstanding)
    print("Updated inventory:", updated_inventory)
    print("Record status: Consistent")

print("\nReport completed.")
