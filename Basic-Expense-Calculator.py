def main():
    expenses = {}
    while True:
        print("\n--- Expense Calculator ---")
        print("1. Add Expense")
        print("2. View Total Expenses")
        print("3. View Expenses by Category")
        print("4. Reset All Expenses")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            category = input("Enter the category of the expense: ").capitalize()
            amount = float(input("Enter the amount: "))
            if category in expenses:
                expenses[category] += amount
            else:
                expenses[category] = amount
            print(f"Added {amount} to {category}.")
        elif choice == '2':
            total = sum(expenses.values())
            print(f"Total expenses: ${total:}")
        elif choice == '3':
            for category, amount in expenses.items():
                print(f"{category}: ${amount:}")
        elif choice == '4':
            expenses.clear()
            print("All expenses have been reset.")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()