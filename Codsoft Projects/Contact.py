
class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone Number: {self.phone_number}\nEmail: {self.email}\nAddress: {self.address}\n"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contact = Contact(name, phone_number, email, address)
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found!")
        else:
            for i, contact in enumerate(self.contacts, 1):
                print(f"Contact {i}:")
                print(contact)
                print()

    def search_contact(self):
        search_term = input("Enter name or phone number to search: ")
        found = False
        for contact in self.contacts:
            if search_term in [contact.name, contact.phone_number]:
                print(contact)
                found = True
        if not found:
            print("Contact not found!")

    def update_contact(self):
        search_term = input("Enter name or phone number to update: ")
        found = False
        for contact in self.contacts:
            if search_term in [contact.name, contact.phone_number]:
                print("Enter new details:")
                contact.name = input("Enter name: ")
                contact.phone_number = input("Enter phone number: ")
                contact.email = input("Enter email: ")
                contact.address = input("Enter address: ")
                print("Contact updated successfully!")
                found = True
                break
        if not found:
            print("Contact not found!")

    def delete_contact(self):
        search_term = input("Enter name or phone number to delete: ")
        found = False
        for contact in self.contacts:
            if search_term in [contact.name, contact.phone_number]:
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                found = True
                break
        if not found:
            print("Contact not found!")


def main():
    contact_book = ContactBook()
    while True:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            contact_book.add_contact()
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            contact_book.search_contact()
        elif choice == "4":
            contact_book.update_contact()
        elif choice == "5":
            contact_book.delete_contact()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()