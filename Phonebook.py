phone_book ={}
def add_contact():
    name = input("Enter the name :").strip().lower()
    phone_num = int(input("Enter the phone number :").strip())
    phone_book[name] = phone_num
    print()
    print()
    print("---------- Contact saved sucessfully!------")
   
def read_contact():
    search_name = input("Enter the searching name :").strip().lower()
    if search_name in phone_book.keys():
        print()
        print('------------------------')
        print(f"The number for {search_name.capitalize()} is : {phone_book[search_name]}")
    else:
        print("Contact is not avaialble...!")
def update_contact():
    update_name = input("Enter the name").strip().lower()
    update_number = int(input("Enter the new number to update :".strip()))
    phone_book[update_name] = update_number
    print()
    print()
    print("---------- Contact saved sucessfully!------")
    
def main():
    while(True):
        print()
        print("Choose the task from the below  options")
        print("""
              1. Add Contact
              2. Read Contact
              3. Update Contact
              4. Delete Contact""")
        print()
        choice = int(input("Enter the choice"))
        if choice == 1:
            add_contact()
        elif choice == 2:
            read_contact()
        elif choice == 3:
            update_contact()
        else:
            break

if __name__=='__main__':
    main()
