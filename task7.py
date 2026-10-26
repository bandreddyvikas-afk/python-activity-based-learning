
students = ["A", "B", "C", "D", "E", "F"]
scores = [95, 90, 85, 80, 75, 70]

group_sizes = [2, 2, 2]
groups = []
totals = []

# Create empty groups
for size in group_sizes:
    groups.append([])
    totals.append(0)

# Sort students by score in descending order
students_scores = list(zip(students, scores))
students_scores.sort(key=lambda x: x[1], reverse=True)

# Allocate students to the group with the lowest total
for student, score in students_scores:
    best = -1

    for i in range(len(groups)):
        if len(groups[i]) < group_sizes[i]:
            if best == -1 or totals[i] < totals[best]:
                best = i

    groups[best].append((student, score))
    totals[best] += score

# Display results
print("STUDENT GROUP ALLOCATION")
print("-" * 35)

for i in range(len(groups)):
    print("Group", i + 1)
    for student, score in groups[i]:
        print(student, ":", score)
    print("Total score:", totals[i])
    print()

difference = max(totals) - min(totals)
print("Difference between group totals:", difference)
