import csv

FILE_NAME = "expenses.csv"


def add_expense():
    name = input("Enter expense name: ")
    category = input("Enter category (Food/Travel/etc): ")
    amount = input("Enter amount: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, category, amount])

    print("Expense added successfully.\n")


def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            print("\nExpenses:")
            for i, row in enumerate(reader, start=1):
                print(f"{i}. {row[0]} | {row[1]} | ${row[2]}")
            print()

    except FileNotFoundError:
        print("No expenses recorded yet.\n")


def total_expense():
    total = 0

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                total += float(row[2])

        print(f"\nTotal expenses: ${total}\n")

    except FileNotFoundError:
        print("No expenses recorded yet.\n")


def category_summary():
    summary = {}

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                category = row[1]
                amount = float(row[2])

                summary[category] = summary.get(category, 0) + amount

        print("\nCategory Summary:")
        for category, total in summary.items():
            print(f"{category}: ${total}")
        print()

    except FileNotFoundError:
        print("No expenses recorded yet.\n")


def delete_expense():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            expenses = list(reader)

        for i, row in enumerate(expenses, start=1):
            print(f"{i}. {row[0]} | {row[1]} | ${row[2]}")

        choice = int(input("Enter expense number to delete: "))
        expenses.pop(choice - 1)

        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(expenses)

        print("Expense deleted successfully.\n")

    except FileNotFoundError:
        print("No expenses recorded yet.\n")


def search_expense():
    keyword = input("Enter expense name to search: ")

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            found = False

            for row in reader:
                if keyword.lower() in row[0].lower():
                    print(f"{row[0]} | {row[1]} | ${row[2]}")
                    found = True

            if not found:
                print("No matching expense found.\n")

    except FileNotFoundError:
        print("No expenses recorded yet.\n")


def menu():
    while True:

        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total")
        print("4. Category Summary")
        print("5. Delete Expense")
        print("6. Search Expense")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expense()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            delete_expense()

        elif choice == "6":
            search_expense()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option.\n")


menu()