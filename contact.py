class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        print("Contact List:")
        for index, contact in enumerate(self.contacts):
            print(f"{index+1}. {contact.name} - {contact.phone}")

    def search_contact(self):
        keyword = input("Enter name or phone number to search: ")
        results = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone:
                results.append(contact)
        if results:
            print("Search Results:")
            for contact in results:
                print(f"- {contact.name} - {contact.phone}")
        else:
            print("No contacts found.")

    def update_contact(self):
        name_to_update = input("Enter the name of the contact to update: ")
        for contact in self.contacts:
            if contact.name == name_to_update:
                print("Enter new details:")
                contact.phone = input("New Phone: ") or contact.phone
                contact.email = input("New Email: ") or contact.email
                contact.address = input("New Address: ") or contact.address
                print("Contact updated successfully!")
                return
        print("Contact not found.")

    def delete_contact(self):
        name_to_delete = input("Enter the name of the contact to delete: ")
        for contact in self.contacts:
            if contact.name == name_to_delete:
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                return
        print("Contact not found.")

if __name__ == "__main__":
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            contact_book.add_contact()
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            contact_book.search_contact()
        elif choice == '4':
            contact_book.update_contact()
        elif choice == '5':
            contact_book.delete_contact()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            
            