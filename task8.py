
routes = ["Route A", "Route B", "Route C"]
demand = [135, 80, 210]
capacity = [50, 40, 60]
available_buses = [2, 2, 3]

print("BUS REQUIREMENT ANALYSIS")
print("-" * 75)
print(f"{'Route':<12}{'Demand':<10}{'Capacity':<12}"
      f"{'Buses Used':<12}{'Unserved':<10}")

for i in range(len(routes)):
    # Calculate buses required
    required = (demand[i] + capacity[i] - 1) // capacity[i]

    # Use only the available buses
    buses_used = min(required, available_buses[i])

    # Calculate available seats and unserved passengers
    seats = buses_used * capacity[i]
    unserved = max(0, demand[i] - seats)

    print(f"{routes[i]:<12}{demand[i]:<10}{capacity[i]:<12}"
          f"{buses_used:<12}{unserved:<10}")

    if unserved > 0:
        print("  ALERT: More buses are needed!")

print("-" * 75)
