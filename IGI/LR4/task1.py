import csv
import pickle

class SavableMixin:
    """
    A class that provides methods for saving and loading data to/from different file formats.
    """

    def save_to_csv(self, filename, data):
        """
        Saves the given data to a CSV file.

        Args:
            filename (str): The name of the CSV file to save.
            data (dict): The data to be saved.

        Returns:
            None
        """
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            for item in data.items():
                writer.writerow(item)

    def load_from_csv(self, filename):
        """
        Loads data from a CSV file.

        Args:
            filename (str): The name of the CSV file to load.

        Returns:
            dict: The loaded data.
        """
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            return {rows[0]: rows[1] for rows in reader}

    def save_to_pickle(self, filename, data):
        """
        Saves the given data to a pickle file.

        Args:
            filename (str): The name of the pickle file to save.
            data (object): The data to be saved.

        Returns:
            None
        """
        with open(filename, 'wb') as f:
            pickle.dump(data, f)

    def load_from_pickle(self, filename):
        """
        Loads data from a pickle file.

        Args:
            filename (str): The name of the pickle file to load.

        Returns:
            object: The loaded data.
        """
        with open(filename, 'rb') as f:
            return pickle.load(f)

class PhoneBook(SavableMixin):
    """
    A class representing a phone book.

    Attributes:
        entries (dict): A dictionary containing the phone book entries, where the keys are names and the values are phone numbers.

    Methods:
        add_entry(name, phone_number): Adds a new entry to the phone book.
        search(starting_digits): Searches for entries in the phone book that have phone numbers starting with the specified digits.
        sort_entries(): Sorts the phone book entries alphabetically by name.
        save_to_csv(filename): Saves the phone book entries to a CSV file.
        load_from_csv(filename): Loads phone book entries from a CSV file.
        save_to_pickle(filename): Saves the phone book entries to a pickle file.
        load_from_pickle(filename): Loads phone book entries from a pickle file.
    """

    def __init__(self):
        super().__init__()
        self.entries = {}

    def add_entry(self, name, phone_number):
        """
        Adds a new entry to the phone book.

        Args:
            name (str): The name of the entry.
            phone_number (str): The phone number associated with the entry.
        """
        self.entries[name] = phone_number

    def search(self, starting_digits):
        """
        Searches for entries in the phone book that have phone numbers starting with the specified digits.

        Args:
            starting_digits (str): The digits that the phone numbers should start with.

        Returns:
            dict: A dictionary containing the matching entries, where the keys are names and the values are phone numbers.
        """
        return {name: phone for name, phone in self.entries.items() if phone.startswith(starting_digits)}

    def sort_entries(self):
        """
        Sorts the phone book entries alphabetically by name.
        """
        self.entries = dict(sorted(self.entries.items()))

    def save_to_csv(self, filename):
        """
        Saves the phone book entries to a CSV file.

        Args:
            filename (str): The name of the CSV file to save the entries to.
        """
        super().save_to_csv(filename, self.entries)

    def load_from_csv(self, filename):
        """
        Loads phone book entries from a CSV file.

        Args:
            filename (str): The name of the CSV file to load the entries from.
        """
        self.entries = super().load_from_csv(filename)

    def save_to_pickle(self, filename):
        """
        Saves the phone book entries to a pickle file.

        Args:
            filename (str): The name of the pickle file to save the entries to.
        """
        super().save_to_pickle(filename, self.entries)

    def load_from_pickle(self, filename):
        """
        Loads phone book entries from a pickle file.

        Args:
            filename (str): The name of the pickle file to load the entries from.
        """
        self.entries = super().load_from_pickle(filename)


def task_1():
    # Create a new phone book
    phonebook = PhoneBook()

    while True:
        print("\n1. Add entry")
        print("2. Search")
        print("3. Sort entries")
        print("4. Save to CSV")
        print("5. Load from CSV")
        print("6. Save to Pickle")
        print("7. Load from Pickle")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            phonebook.add_entry(name, phone_number)

        elif choice == '2':
            starting_digits = input("Enter starting digits: ")
            print(phonebook.search(starting_digits))

        elif choice == '3':
            phonebook.sort_entries()

        elif choice == '4':
            filename = input("Enter filename: ")
            phonebook.save_to_csv(filename)

        elif choice == '5':
            filename = input("Enter filename: ")
            phonebook.load_from_csv(filename)

        elif choice == '6':
            filename = input("Enter filename: ")
            phonebook.save_to_pickle(filename)

        elif choice == '7':
            filename = input("Enter filename: ")
            phonebook.load_from_pickle(filename)

        elif choice == '8':
            break

        else:
            print("Invalid choice. Please try again.")