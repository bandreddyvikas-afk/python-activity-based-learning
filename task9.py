
# Seating Matrix Validation

seating = [
    ["R101", "R102", None],
    ["R103", "R101", "R999"],
    ["R105", "R106", "R107"]
]

valid_rolls = ["R101", "R102", "R103", "R104",
               "R105", "R106", "R107", "R108"]

# Reserved seat positions (row, column), starting from 1
reserved = [(2, 2)]

seen = set()
duplicates = set()
errors = 0

print("SEATING MATRIX VALIDATION")
print("-" * 35)

for i in range(len(seating)):
    for j in range(len(seating[i])):
        roll = seating[i][j]
        position = (i + 1, j + 1)

        if position in reserved:
            if roll is not None:
                print("Reserved seat occupied:", position, roll)
                errors += 1
            continue

        if roll is None or roll == "":
            print("Empty seat:", position)
            errors += 1

        elif roll not in valid_rolls:
            print("Invalid roll number:", roll, "at", position)
            errors += 1

        elif roll in seen:
            if roll not in duplicates:
                print("Duplicate roll number:", roll)
                duplicates.add(roll)
                errors += 1

        else:
            seen.add(roll)

print("-" * 35)
print("Total validation errors:", errors)
