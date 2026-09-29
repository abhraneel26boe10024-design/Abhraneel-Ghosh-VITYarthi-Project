# VIT Bhopal Healcare Campaign System

students =[]

campaign = [{"Name":"Health Awareness Camp", "Date":"03-10-2026", "Time":"10:30 AM", "Venue":"Academic Block 2 1st Floor"}
            ,{"Name":"Nutrition Awareness Camp", "Date":"03-10-2026","Time":"12:30 PM", "Venue":"Academic Block 1 1st Floor"}
            ,{"Name":"Mental Health Awareness Camp", "Date":"03-10-2026", "Time":"02:30 PM", "Venue":"Academic Block 3 1st Floor"}
            ,{"Name":"Blood Donation Camp", "Date":"03-10-2026", "Time":"4:30 PM", "Venue":"Academic Block 2 2nd Floor"}
            ,{"Name":"Drug Abuse Prevention & Awareness Campaign", "Date":"04-10-2026", "Time":"10:30 AM", "Venue":"Academic Block 3 Auditorium"}]

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


# Health Awareness Information
def display_health_awareness():
    print("\n---Health Awareness Information---")

    print("1.Maintain proper hygiene.")
    print("2.Eat a balanced and nutritious diet.")
    print("3.Stay physically active.")
    print("4.Get adequate sleep.")
    print("5.Drink enough water.")
    print("6.Seek professional medical help when needed.")
    print("7.Avoid tobacco,alcohol and drugs")
    print("8.Practice good mental health")
    print("9.Take recommended vaccination on time")

# Display Campaign
def view_campaign():
  print("\n---Upcoming Healthcare Campaign---")

  for i, Campaign in enumerate(campaign,start=1):

     print("\nCampaign",i)
     print("Name:",Campaign["Name"])
     print("Date:",Campaign["Date"])
     print("Time:",Campaign["Time"])
     print("Venue:",Campaign["Venue"])


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

#Main program
while True:

     print("\n==============================")
     print("VIT BHOPAL HEALTHCARE CAMPAIGN")
     print("==============================")

     print("1. Student Registration")
     print("2. Health Awareness")
     print("3. View Campaign")
     print("4. Register for Campaign")
     print("5. Display Students")
     print("6. Exit")

     choice = input("\nEnter your choice:")

     if choice == "1":
      register_student()

     elif choice == "2":
      display_health_awareness()

     elif choice == "3":
      view_campaign()

     elif choice == "4":
      register_campaign()

     elif choice == "5":
      display_students()

     elif choice == "6":
       print("\nThank you for using Vidyarthi Healthcare Campaign System!")

       break

     else:
       print("\nInvalid choice. Please try again.")
