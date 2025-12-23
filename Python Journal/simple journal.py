from datetime import datetime

JOURNAL_FILE = "journal.txt"

def add_entry():
    entry = input("\nWrite your journal entry:\n> ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open(JOURNAL_FILE, "a", encoding="utf-8") as file:
        file.write("\n--------------------\n")
        file.write(timestamp + "\n")
        file.write(entry + "\n")

    print("\nEntry saved!")

def view_entries():
    try:
        with open(JOURNAL_FILE, "r", encoding="utf-8") as file:
            print("\nYour Journal:\n")
            print(file.read())
    except FileNotFoundError:
        print("\nNo journal entries yet.")

def menu():
    while True:
        print("\n--- Journal App ---")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

menu()
