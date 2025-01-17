import datetime
from collections import defaultdict

# Initialize global variables
expenses = []
categories = ['Food', 'Transportation', 'Entertainment', 'Bills', 'Other']

def add_expense(amount, category, description, date=None):
    
    if date is None:
        date = datetime.date.today()
    
    if category not in categories:
        return f"Invalid category. Please choose from: {', '.join(categories)}"
        
    expense = {
        'date': date,
        'amount': amount,
        'category': category,
        'description': description
    }
    expenses.append(expense)
    return "Expense added successfully!"

def view_expenses():

    if not expenses:
        return "No expenses recorded yet."
        
    output = "\nAll Expenses:\n"
    output += "-" * 60 + "\n"
    output += "Date\t\tAmount\t\tCategory\tDescription\n"
    output += "-" * 60 + "\n"
    
    for expense in sorted(expenses, key=lambda x: x['date']):
        output += f"{expense['date']}\t₹{expense['amount']:.2f}\t\t{expense['category']}\t{expense['description']}\n"
    
    return output

def get_category_totals():
    
    category_totals = defaultdict(float)
    
    for expense in expenses:
        category_totals[expense['category']] += expense['amount']
        
    output = "\nExpense Totals by Category:\n"
    output += "-" * 30 + "\n"
    
    for category in categories:
        output += f"{category}: ₹{category_totals[category]:.2f}\n"
        
    return output

def get_total_expenses():

    return sum(expense['amount'] for expense in expenses)

# Interactive menu
while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Category Totals")
    print("4. View Total Expenses")
    print("5. Exit")
    
    choice = input("\nEnter your choice: ")
    choice = choice.lower()
    
    if choice == '1' or choice == "add expense":
        try:
            amount = float(input("Enter amount: ₹"))
            print("\nCategories:", ', '.join(categories))
            category = input("Enter category: ")
            description = input("Enter description: ")
            
            result = add_expense(amount, category, description)
            print(result)
        except ValueError:
            print("Invalid amount. Please enter a number.")
            
    elif choice == '2' or choice == "view all expense":
        print(view_expenses())
        
    elif choice == '3' or choice == "view category total":
        print(get_category_totals())
        
    elif choice == '4' or choice == "view total expenses":
        total = get_total_expenses()
        print(f"\nTotal Expenses: ₹{total:.2f}")
        
    elif choice == '5':
        print("Thank you for using Expense Tracker!")
        break
        
    else:
        print("Invalid choice. Please try again.")