class Transaction:
    def __init__(self, date, time, amount_spent, merchant, tag, id = None):
        self.date = date
        self.time = time
        self.amount_spent = amount_spent
        self.merchant = merchant
        self.tag = tag
        self.id = id
