"""
Expense Tracker System - Task 3 & Task 4
Testing and Quality Assurance Project
Author: Sailaja Injarapu
"""

import os

class Expense:
    """Stores one expense details"""
    def __init__(self, item, amount, date):
        self.item = item
        self.amount = amount
        self.date = date

class ExpenseTracker:
    def __init__(self, filename="expenses.txt"):
        self.filename = filename
        self.expenses = []
        self.load_from_file()

    def add_expense(self, item, amount):
        """Add new expense - Returns True if added, False if invalid"""
        try:
            if not item or item.strip() == "":
                print("Error: Invalid input")
                return False
            amount = int(amount)
            if amount < 0:
                print("Amount cannot be negative")
                return False
            if amount == 0:
                print("Error: Invalid input")
                return False
            from datetime import date
            today = str(date.today())
            exp = Expense(item, amount, today)
            self.expenses.append(exp)
            self.save_to_file()
            print(f"Expense Added: {item} - Rs.{amount}")
            return True
        except ValueError:
            print("Please enter valid number")
            return False

    def view_expenses(self):
        """Show all expenses"""
        if len(self.expenses) == 0:
            print("No expenses found")
            return []
        for i, e in enumerate(self.expenses, 1):
            print(f"{i}. {e.item} - Rs.{e.amount} | Date: {e.date}")
        return self.expenses

    def delete_expense(self, item):
        """Delete expense by name"""
        for e in self.expenses:
            if e.item.lower() == item.lower():
                self.expenses.remove(e)
                self.save_to_file()
                print(f"Deleted: {item}")
                return True
        print("Item not found")
        return False

    def calculate_total(self):
        """Calculate total expenses"""
        total = sum(e.amount for e in self.expenses)
        print(f"Total Expenses: Rs.{total}")
        return total

    def save_to_file(self):
        """Save to file"""
        try:
            with open(self.filename, "w") as f:
                for e in self.expenses:
                    f.write(f"{e.item},{e.amount},{e.date}\n")
        except Exception as ex:
            print(f"Error saving file: {ex}")

    def load_from_file(self):
        """Load from file - Handles FileNotFoundError"""
        try:
            if not os.path.exists(self.filename):
                return
            with open(self.filename, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        self.expenses.append(Expense(parts[0], int(parts[1]), parts[2]))
        except FileNotFoundError:
            print("File not found, creating new file")
        except ValueError:
            print("Please enter valid number")

def main():
    tracker = ExpenseTracker()
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Calculate Total")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            item = input("Enter item: ")
            amount = input("Enter amount: ")
            tracker.add_expense(item, amount)
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            item = input("Enter item to delete: ")
            tracker.delete_expense(item)
        elif choice == "4":
            tracker.calculate_total()
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()