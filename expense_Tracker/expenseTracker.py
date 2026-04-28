import os
from datetime import date

def save_expenses():
    with open("expenses.csv", "w") as file:
        file.write("Amount,Category,Date,Note\n")
        for expense in expenses:
            line = f"{expense['Amount']},{expense['Category']},{expense['Date']},{expense['Note']}\n"
            file.write(line)

def load_expenses():
    if not os.path.exists("expenses.csv"):
        return
    with open("expenses.csv","r") as file:
        next(file)
        for line in file:
            data = line.strip().split(",")
            expense = {
                "Amount" : float(data[0]),
                "Category" : data[1],
                "Date" : data[2],
                "Note" : data[3]
            }
            expenses.append(expense)

expenses = []

def expense_tracker():
    load_expenses()
    print("Welcome to Daily Expense Tracker !\n")
    while True:
        print("\nChoose the option :")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Total Spendings")
        print("4. Category Summary")
        print("5. Exit")
        choice = input("Enter you Choice : ")
        if choice == "1":
            print("Adding Expense ")
            amount = float(input("Enter the amount spent : "))
            category = input("Enter the category : ")
            expense_date = input("Enter the date (YYYY-MM-DD) or press Enter for today: ")
            if expense_date == "":
                expense_date = str(date.today())
            note = input("Add note : ")
            expense = {
                "Amount" : amount,
                "Category" : category.title(),
                "Date" : expense_date,
                "Note" : note
            }
            expenses.append(expense)
            print("Expense Added !")

        elif choice == "2":
            print("\nYour Expenses : ")
            if len(expenses) == 0:
                print("Empty !")
            else:
                for i,expense in enumerate(expenses, start=1):
                    print(f"{i}. Amount : {expense['Amount']} | Category : {expense['Category']} | Date : {expense['Date']} | Note : {expense['Note']}")

        elif choice == "3":
            total_spendings = 0
            if len(expenses) == 0:
                print("No spendings !")
            else:
                for expense in expenses:
                    total_spendings += expense["Amount"]
                print(f"\nTotal Spendings are Rupees{total_spendings: .2f}")

        elif choice == "4":
            category_totals = {}
            for expense in expenses:
                category = expense["Category"]
                if category not in category_totals:
                    category_totals[category] = 0
                category_totals[category] += expense["Amount"]

            for cat, total in category_totals.items():
                print()
                print(f"{cat}: {total}")

        elif choice == "5":
            print("Closing..")
            save_expenses()
            break
        
expense_tracker()