# Register for Campaign
def register_campaign():
   print("\n---Campaign Registration---")


   if len(students) == 0:

     print("Please register as a student first.")

     return

   reg_no = input("Enter your registration number:")

   found = False

   for student in students:

    if student["registration_no"] == reg_no:
      found = True

      print("\nWelcome",student["name"])

      view_campaign()

      try:

       choice = int(input("\nSelect campaign number:"))

       if 1 <= choice <= len(campaign):
            print("Successfully registered for:",campaign[choice-1]["Name"])

       else:
            print("Invalid campaign number.")

      except ValueError:
          print("Please enter a valid number.")

      break

    if not found:
     print("Student not found. Please register first.")

