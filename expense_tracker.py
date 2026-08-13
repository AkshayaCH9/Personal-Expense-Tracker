import csv
import os
from datetime import datetime


class Expense:
    def __init__(self, expense_id, date, category, amount, description):
        self.expense_id = expense_id
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def to_list(self):
        return [
            self.expense_id,
            self.date,
            self.category,
            self.amount,
            self.description
        ]


class ExpenseTracker:
    FILE_NAME = "expenses.csv"

    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        if not os.path.exists(self.FILE_NAME):
            return

        try:
            with open(self.FILE_NAME, "r", newline="") as file:
                reader = csv.reader(file)
                next(reader, None)

                for row in reader:
                    if len(row) == 5:
                        expense = Expense(
                            int(row[0]),
                            row[1],
                            row[2],
                            float(row[3]),
                            row[4]
                        )
                        self.expenses.append(expense)

        except (ValueError, OSError) as error:
            print(f"Error loading expenses: {error}")

    def save_expenses(self):
        try:
            with open(self.FILE_NAME, "w", newline="") as file:
                writer = csv.writer(file)

                writer.writerow(
                    ["ID", "Date", "Category", "Amount", "Description"]
                )

                for expense in self.expenses:
                    writer.writerow(expense.to_list())

        except OSError as error:
            print(f"Error saving expenses: {error}")

    def add_expense(self):
        print("\n----- ADD EXPENSE -----")

        while True:
            try:
                amount = float(input("Enter amount: "))

                if amount <= 0:
                    print("Amount must be greater than 0.")
                    continue

                break

            except ValueError:
                print("Please enter a valid number.")

        category = input("Enter category: ").strip().title()

        while not category:
            print("Category cannot be empty.")
            category = input("Enter category: ").strip().title()

        description = input("Enter description: ").strip()

        expense_id = (
            max((expense.expense_id for expense in self.expenses), default=0)
            + 1
        )

        date = datetime.now().strftime("%d-%m-%Y")

        expense = Expense(
            expense_id,
            date,
            category,
            amount,
            description
        )

        self.expenses.append(expense)
        self.save_expenses()

        print("Expense added successfully!")

    def view_expenses(self):
        print("\n----- ALL EXPENSES -----")

        if not self.expenses:
            print("No expenses found.")
            return

        print(
            f"{'ID':<5}"
            f"{'Date':<15}"
            f"{'Category':<15}"
            f"{'Amount':<12}"
            f"Description"
        )

        print("-" * 70)

        for expense in self.expenses:
            print(
                f"{expense.expense_id:<5}"
                f"{expense.date:<15}"
                f"{expense.category:<15}"
                f"₹{expense.amount:<11.2f}"
                f"{expense.description}"
            )

    def search_by_category(self):
        print("\n----- SEARCH BY CATEGORY -----")

        category = input("Enter category: ").strip().lower()

        matching_expenses = [
            expense
            for expense in self.expenses
            if expense.category.lower() == category
        ]

        if not matching_expenses:
            print("No expenses found for this category.")
            return

        total = 0

        for expense in matching_expenses:
            print(
                f"{expense.date} | "
                f"{expense.category} | "
                f"₹{expense.amount:.2f} | "
                f"{expense.description}"
            )
            total += expense.amount

        print(f"\nTotal for {category.title()}: ₹{total:.2f}")

    def total_spending(self):
        print("\n----- TOTAL SPENDING -----")

        total = sum(expense.amount for expense in self.expenses)

        print(f"Total Spending: ₹{total:.2f}")

    def category_summary(self):
        print("\n----- CATEGORY SUMMARY -----")

        if not self.expenses:
            print("No expenses available.")
            return

        summary = {}

        for expense in self.expenses:
            summary[expense.category] = (
                summary.get(expense.category, 0) + expense.amount
            )

        for category, amount in sorted(
            summary.items(),
            key=lambda item: item[1],
            reverse=True
        ):
            print(f"{category:<15} ₹{amount:.2f}")

        highest_category = max(summary, key=summary.get)

        print(
            f"\nHighest Spending Category: "
            f"{highest_category}"
        )

    def delete_expense(self):
        print("\n----- DELETE EXPENSE -----")

        if not self.expenses:
            print("No expenses available.")
            return

        self.view_expenses()

        try:
            expense_id = int(input("\nEnter expense ID to delete: "))

            for expense in self.expenses:
                if expense.expense_id == expense_id:
                    self.expenses.remove(expense)
                    self.save_expenses()
                    print("Expense deleted successfully!")
                    return

            print("Expense ID not found.")

        except ValueError:
            print("Please enter a valid expense ID.")

    def run(self):
        while True:
            print("\n")
            print("=" * 40)
            print("       PERSONAL EXPENSE TRACKER")
            print("=" * 40)
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Search by Category")
            print("4. Total Spending")
            print("5. Category Summary")
            print("6. Delete Expense")
            print("7. Exit")
            print("=" * 40)

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_expense()

            elif choice == "2":
                self.view_expenses()

            elif choice == "3":
                self.search_by_category()

            elif choice == "4":
                self.total_spending()

            elif choice == "5":
                self.category_summary()

            elif choice == "6":
                self.delete_expense()

            elif choice == "7":
                print("Thank you for using Personal Expense Tracker!")
                break

            else:
                print("Invalid choice. Please select 1-7.")


if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()