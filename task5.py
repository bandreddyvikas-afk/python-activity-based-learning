
# Passenger Boarding and Alighting System

capacity = int(input("Enter bus capacity: "))
passengers = int(input("Enter initial passengers: "))
stops = int(input("Enter number of stops: "))

for i in range(1, stops + 1):
    print("\nStop", i)

    boarding = int(input("Passengers boarding: "))
    alighting = int(input("Passengers alighting: "))

    if boarding < 0 or alighting < 0:
        print("Invalid passenger count!")
        continue

    if alighting > passengers:
        print("Error: More passengers alighting than onboard!")
        continue

    passengers = passengers - alighting + boarding

    print("Passengers after stop:", passengers)

    if passengers > capacity:
        print("Capacity Violation!")
    else:
        print("Capacity is within limit.")

print("\nFinal passenger count:", passengers)
