from transaction import Transaction
from storage import load_transactions, save_transactions



class ExpenseTracker:


    def __init__(self):

        self.transactions = load_transactions()



    # Add Income / Expense

    def add_transaction(self):

        print("\nAdd New Transaction")


        title = input("Enter title: ")

        amount = float(input("Enter amount (Rs.): "))

        category = input("Enter category: ")

        date = input("Enter date (DD-MM-YYYY): ")


        print("""
1. Income
2. Expense
""")


        choice = input("Select type: ")


        if choice == "1":

            transaction_type = "Income"


        elif choice == "2":

            transaction_type = "Expense"


        else:

            print("Invalid type")

            return



        notes = input("Enter notes: ")



        new_transaction = Transaction(

            title,
            amount,
            category,
            date,
            transaction_type,
            notes

        )



        self.transactions.append(

            new_transaction.to_dictionary()

        )



        save_transactions(self.transactions)



        print("\nTransaction Added Successfully")






    # View all transactions

    def view_transactions(self):


        if len(self.transactions) == 0:

            print("\nNo transactions found")

            return



        print("\nAll Transactions")



        for transaction in self.transactions:


            print("-----------------------------")

            print("Title:", transaction["title"])

            print("Amount: Rs.", transaction["amount"])

            print("Category:", transaction["category"])

            print("Date:", transaction["date"])

            print("Type:", transaction["type"])

            print("Notes:", transaction["notes"])

            print("-----------------------------")






    # Search transaction

    def search_transactions(self):


        search_word = input(
            "Enter search word: "
        ).lower()



        found = False



        for transaction in self.transactions:


            if (

                search_word in transaction["title"].lower()

                or

                search_word in transaction["category"].lower()

                or

                search_word in transaction["notes"].lower()

            ):



                print("-----------------------------")

                print("Title:", transaction["title"])

                print("Amount: Rs.", transaction["amount"])

                print("Category:", transaction["category"])

                print("Date:", transaction["date"])

                print("Type:", transaction["type"])

                print("Notes:", transaction["notes"])

                print("-----------------------------")


                found = True





        if found == False:

            print("No matching transaction found")






    # Filter by category

    def filter_by_category(self):


        category = input(
            "Enter category: "
        ).lower()



        found = False



        for transaction in self.transactions:


            if transaction["category"].lower() == category:



                print("-----------------------------")

                print("Title:", transaction["title"])

                print("Amount: Rs.", transaction["amount"])

                print("Date:", transaction["date"])

                print("Type:", transaction["type"])

                print("Notes:", transaction["notes"])

                print("-----------------------------")


                found = True





        if found == False:

            print("No transaction found for this category")







    # Filter by date

    def filter_by_date(self):


        date = input(
            "Enter date (DD-MM-YYYY): "
        )



        found = False



        for transaction in self.transactions:


            if transaction["date"] == date:



                print("-----------------------------")

                print("Title:", transaction["title"])

                print("Amount: Rs.", transaction["amount"])

                print("Category:", transaction["category"])

                print("Type:", transaction["type"])

                print("Notes:", transaction["notes"])

                print("-----------------------------")


                found = True





        if found == False:

            print("No transaction found on this date")