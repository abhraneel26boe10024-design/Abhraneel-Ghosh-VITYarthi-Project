#Student Registration
def register_student():
    global students 
    print("\n---Student Registration---")

    name = input("Enter your name:")
    registration_no = input("Enter your registration number:")
    branch = input("Enter your branch:")
    student_type = input("Enter your type (Hosteller or Day Scholar):")

    # duplicate registration
    for existing_student in students:

      if existing_student["registration_no"] == registration_no:

        print("Registration number already exists. Please choose a different one.")

        return

    student = {"name": name, "registration_no": registration_no, "branch": branch, "student_type": student_type}

    students.append(student)

    print("Registration successful!")
