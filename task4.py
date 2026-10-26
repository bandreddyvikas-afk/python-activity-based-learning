
# Student Marks Matrix Analysis

students = ["Ravi", "Sita", "Kiran", "Anu", "Rahul"]
subjects = ["Python", "Maths", "English", "Physics"]

marks = [
    [85, 90, 78, 88],
    [92, 95, 89, 94],
    [60, 55, 65, 58],
    [75, 80, 72, 70],
    [88, 85, 91, 86]
]

# Row-wise statistics
print("STUDENT-WISE ANALYSIS")
averages = []

for i in range(len(marks)):
    total = sum(marks[i])
    avg = total / len(subjects)
    averages.append(avg)

    print(students[i], "Total:", total,
          "Average:", round(avg, 2))

# Identify top performer
top_index = averages.index(max(averages))
print("\nTop Performer:", students[top_index])
print("Highest Average:", round(averages[top_index], 2))

# Column-wise statistics
print("\nSUBJECT-WISE ANALYSIS")
subject_averages = []

for j in range(len(subjects)):
    column = [marks[i][j] for i in range(len(marks))]
    avg = sum(column) / len(column)
    subject_averages.append(avg)

    print(subjects[j], "Average:", round(avg, 2))

# Identify low-performing subjects
threshold = 70
print("\nLOW-PERFORMING SUBJECTS")

found = False
for j in range(len(subjects)):
    if subject_averages[j] < threshold:
        print(subjects[j])
        found = True

if not found:
    print("No low-performing subjects")
