# Display Registered Students:
def display_students():
     print("\n---Registered Students---")

     if len(students) == 0:
       print("No students registered yet.")

       return

     for student in students:

       print("\nName:", student["name"])
       print("Reg No.:", student["registration_no"])
       print("Branch:", student["branch"])
       print("Student Type:", student["student_type"])
