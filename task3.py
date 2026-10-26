students = [
    "24IT001",
    "25CS012",
    "24EC025",
    "23IT105",
    "26XX001",
    "24IT"
]

branch_names = {
    "IT": "Information Technology",
    "CS": "Computer Science",
    "EC": "Electronics"
}

for sid in students:
    if (len(sid) == 7 and
        sid[:2].isdigit() and
        sid[2:4].isalpha() and
        sid[4:].isdigit()):

        year = sid[:2]
        branch = sid[2:4]
        number = sid[4:]

        if branch in branch_names:
            print("Valid ID:", sid)
            print("Admission year: 20" + year)
            print("Branch:", branch_names[branch])
            print("Student number:", number)
        else:
            print("Invalid branch code:", sid)
    else:
        print("Invalid ID format:", sid)