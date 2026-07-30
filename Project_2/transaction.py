class Transaction:


    def __init__(self, title, amount, category, date, transaction_type, notes):

        self.title = title
        self.amount = amount
        self.category = category
        self.date = date
        self.transaction_type = transaction_type
        self.notes = notes



    def to_dictionary(self):

        transaction = {

            "title": self.title,

            "amount": self.amount,

            "category": self.category,

            "date": self.date,

            "type": self.transaction_type,

            "notes": self.notes

        }


        return transaction