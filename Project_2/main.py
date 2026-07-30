from expense_tracker import ExpenseTracker
from reports import generate_report



tracker = ExpenseTracker()



while True:


    print("""
================================
    PERSONAL EXPENSE TRACKER
================================

1. Add Transaction

2. View All Transactions

3. Search Transactions

4. Filter By Category

5. Filter By Date

6. Generate Report

7. Exit

================================
""")


    choice = input("Enter your choice: ")




    if choice == "1":

        tracker.add_transaction()



    elif choice == "2":

        tracker.view_transactions()



    elif choice == "3":

        tracker.search_transactions()



    elif choice == "4":

        tracker.filter_by_category()



    elif choice == "5":

        tracker.filter_by_date()



    elif choice == "6":

        generate_report(
            tracker.transactions
        )



    elif choice == "7":

        print("\nThank you for using Expense Tracker")

        break



    else:

        print("\nInvalid choice. Try again.")