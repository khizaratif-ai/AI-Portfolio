import json


file_name = "transactions.json"



# Load transactions from JSON file

def load_transactions():

    file = open(file_name, "r")

    data = json.load(file)

    file.close()

    return data





# Save transactions into JSON file

def save_transactions(data):

    file = open(file_name, "w")

    json.dump(data, file, indent=4)

    file.close()