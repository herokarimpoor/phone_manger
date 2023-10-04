from phonebook import PhoneBookManager
from get_params import GetParams
def main():
    phone_book = PhoneBookManager()

    while True:
        print("\n1. Add Contact")
        print("2. Show Contacts")
        print("3 search by name")
        print("4 Delete by name")
        print("5. Save and Exit")
        choice = input("Please select an option: ")

        if choice == '1':
            GetParams.invoke_create_new_number()
        elif choice == '2':
            phone_book.show_contacts()
        elif choice == '3':
            # search by name
            search_name = input('Please enter the name to search for: ')
            search_result = phone_book.search_by_name(search_name)

            if not search_result.empty:
                print('Search result:')
                print(search_result)
                print(search_result)
            else:
                print('No matching records found.')
        elif choice == '4':
            delete_name = input('Please enter the name to delete: ')
            phone_book.delete_by_name(delete_name)

        elif choice == '5':
            file_name = input("Enter the Excel file name to save your contacts: ")
            phone_book.save_and_exit(file_name)
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
