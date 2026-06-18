class ContactManager:
    def __init__(self):
        self.contacts = []

    # Validate phone number
    def validate_phone(self, phone):
        allowed = "+-0123456789"
        for char in phone:
            if char not in allowed:
                return False
        return True

    # Validate email
    def validate_email(self, email):
        if email == "":
            return True
        return "@" in email and "." in email

    # Add contact
    def add_contact(self, name, phone, email=""):
        if not self.validate_phone(phone):
            print("Error: Invalid phone number. Use digits, '+' and hyphens only.")
            return

        if not self.validate_email(email):
            print("Error: Invalid email address.")
            return

        self.contacts.append((name, phone, email))
        print("Contact added successfully.")

    # View contact
    def view_contact(self, name):
        for contact in self.contacts:
            if contact[0].lower() == name.lower():
                print("\nContact Found")
                print(f"Name : {contact[0]}")
                print(f"Phone: {contact[1]}")
                print(f"Email: {contact[2]}")
                return
        print("Contact not found.")

    # Update contact
    def update_contact(self, name, new_phone=None, new_email=None):
        for i, contact in enumerate(self.contacts):
            if contact[0].lower() == name.lower():

                phone = contact[1] if new_phone is None else new_phone
                email = contact[2] if new_email is None else new_email

                if not self.validate_phone(phone):
                    print("Error: Invalid phone number.")
                    return

                if not self.validate_email(email):
                    print("Error: Invalid email address.")
                    return

                self.contacts[i] = (contact[0], phone, email)
                print("Contact updated successfully.")
                return

        print("Contact not found.")

    # Delete contact
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact[0].lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

    # Advanced search
    def search_contacts(self, keyword):
        results = []

        for contact in self.contacts:
            if (
                keyword.lower() in contact[0].lower()
                or keyword.lower() in contact[1].lower()
                or keyword.lower() in contact[2].lower()
            ):
                results.append(contact)

        if results:
            print("\n=== Search Results ===")
            for i, contact in enumerate(results, start=1):
                print(f"\nContact {i}")
                print(f"Name : {contact[0]}")
                print(f"Phone: {contact[1]}")
                print(f"Email: {contact[2]}")
        else:
            print("No matching contacts found.")

    # List all contacts
    def list_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return

        print("\n=== All Contacts ===")
        for i, contact in enumerate(self.contacts, start=1):
            print(f"\nContact {i}")
            print(f"Name : {contact[0]}")
            print(f"Phone: {contact[1]}")
            print(f"Email: {contact[2]}")


def main():
    manager = ContactManager()

    while True:
        print("\n=== Contact Manager Menu ===")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contacts")
        print("6. List All Contacts")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email (optional): ")
            manager.add_contact(name, phone, email)

        elif choice == "2":
            name = input("Enter contact name: ")
            manager.view_contact(name)

        elif choice == "3":
            name = input("Enter contact name to update: ")
            phone = input("Enter new phone (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")

            phone = None if phone == "" else phone
            email = None if email == "" else email

            manager.update_contact(name, phone, email)

        elif choice == "4":
            name = input("Enter contact name to delete: ")
            manager.delete_contact(name)

        elif choice == "5":
            keyword = input("Enter search keyword: ")
            manager.search_contacts(keyword)

        elif choice == "6":
            manager.list_contacts()

        elif choice == "7":
            print("Exiting Contact Manager. Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1 and 7.")


if __name__ == "__main__":
    main()