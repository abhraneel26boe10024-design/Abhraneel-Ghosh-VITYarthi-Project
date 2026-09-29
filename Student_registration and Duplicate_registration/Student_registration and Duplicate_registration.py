#Student Registration
def register_student():
    print("\n---Student Registration---")

    name = input("Enter your name:")
    registration_no = input("Enter your registration number:")
    branch = input("Enter your branch:")
    student_type = input("Enter your type (Hosteller or Day Scholar):")

    # duplicate registration
    for students in students:

      if students["registration_no"] == registration_no:

        print("Registration number already exists. Please choose a different one.")

        return

    student = {"name": name, "registration_no": registration_no, "branch": branch, "student_type": student_type}

    students.append(student)

    print("Registration successful!")
