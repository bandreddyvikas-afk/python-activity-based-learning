
def validate_email(email):
    errors = []

    if email.count("@") != 1:
        errors.append("Malformed @ separator")
    else:
        username, domain = email.split("@")

        if username == "":
            errors.append("Missing username")
        elif not username.replace(".", "").replace("_", "").isalnum():
            errors.append("Invalid username characters")

        if domain == "":
            errors.append("Missing domain")
        elif not domain.endswith(".edu"):
            errors.append("Invalid domain ending")

        if domain.count(".") == 0:
            errors.append("Missing domain separator")

    if " " in email:
        errors.append("Spaces are not allowed")

    return errors


def validate_registration(reg_id):
    errors = []

    if reg_id == "":
        errors.append("Missing registration ID")
    elif not reg_id.startswith("NRI"):
        errors.append("Invalid prefix")
    elif len(reg_id) != 9:
        errors.append("Registration ID must have 9 characters")
    elif not reg_id[3:].isdigit():
        errors.append("Invalid character group: digits required")

    return errors


students = [
    ("student1@college.edu", "NRI123456"),
    ("@college.edu", "ABC123456"),
    ("student@@college.edu", "NRI12AB56"),
    ("student college.com", "NRI12345")
]

for email, reg_id in students:
    email_errors = validate_email(email)
    reg_errors = validate_registration(reg_id)

    print("\nEmail:", email)
    print("Registration ID:", reg_id)

    if not email_errors:
        print("Email: Valid")
    else:
        print("Email errors:", email_errors)

    if not reg_errors:
        print("Registration ID: Valid")
    else:
        print("Registration errors:", reg_errors)
