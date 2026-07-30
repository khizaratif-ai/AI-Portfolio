def generate_report(transactions):


    total_income = 0

    total_expenses = 0


    expense_categories = {}



    for transaction in transactions:



        if transaction["type"] == "Income":


            total_income = total_income + transaction["amount"]



        else:


            total_expenses = total_expenses + transaction["amount"]



            category = transaction["category"]



            if category in expense_categories:


                expense_categories[category] = (
                    expense_categories[category]
                    +
                    transaction["amount"]
                )


            else:


                expense_categories[category] = transaction["amount"]





    print("\n============================")

    print("        EXPENSE REPORT")

    print("============================")



    print(
        "Total Income: Rs.",
        total_income
    )



    print("\nExpenses:")



    if len(expense_categories) == 0:

        print("No expenses recorded")


    else:


        for category in expense_categories:


            print(
                category,
                ": Rs.",
                expense_categories[category]
            )





    print(
        "\nTotal Expenses: Rs.",
        total_expenses
    )




    balance = total_income - total_expenses



    print(
        "Current Balance: Rs.",
        balance
    )


    print("============================")