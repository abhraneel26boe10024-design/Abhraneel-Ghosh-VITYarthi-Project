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
