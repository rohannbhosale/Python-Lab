

contacts = {}

while True:
    print("Select the option :")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit ")

    choice = input("\nEnter the choice :")
    if choice == "1":
        name = input("Enter Name : ")
        phone = input("Enter contact no. : ")
        contacts[name] = phone
    elif choice == "2":
        if len(contacts) == 0:
            print("No Contacts found !")
        else:
            for name, phone in contacts.items():
                print(name,":",phone)
    elif choice == "3":
        search_name = input("Enter the Name to search : ")
        if search_name in contacts:
            print("Number :",contacts[search_name])
        else:
            print("Contact not found !")
    elif choice == "4":
        del_name = input("Enter contact name to delete : ")
        if del_name in contacts:
            del contacts[del_name]
            print("Contact deleted Successfully !")
        else:
            print("Contact not found !")
    elif choice == "5":
        print("Closing Contact Book...")
        break
    else :
        print("Enter valid choice !")