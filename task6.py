
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
prepared = [100, 120, 150, 100, 200]
served = [95, 110, 130, 98, 170]

limit = 10

print("MEAL WASTAGE ANALYSIS")
print("-" * 65)
print(f"{'Day':<12}{'Prepared':<12}{'Served':<12}"
      f"{'Leftovers':<12}{'Wastage %':<12}")

for i in range(len(days)):
    leftovers = prepared[i] - served[i]
    wastage = (leftovers / prepared[i]) * 100

    print(f"{days[i]:<12}{prepared[i]:<12}{served[i]:<12}"
          f"{leftovers:<12}{wastage:.2f}%")

    if wastage > limit:
        print("  ALERT: Wastage exceeds 10%!")

print("-" * 65)
