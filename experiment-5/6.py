"""Create a contact book where users can store, search, update, and delete contacts.
Use dictionary for storing contacts."""

contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")


    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact Added.")


    elif choice == "2":
        name = input("Enter name to search: ")
        if name in contacts:
            print("Phone Number:", contacts[name])
        else:
            print("Contact not found.")


    elif choice == "3":
        name = input("Enter name to update: ")
        if name in contacts:
            phone = input("Enter new phone number: ")
            contacts[name] = phone
            print("Contact Updated.")
        else:
            print("Contact not found.")


    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact Deleted.")
        else:
            print("Contact not found.")


    elif choice == "5":
        print("All Contacts:")
        for i in contacts:
            print(i, "-", contacts[i])


    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid Choice.")
