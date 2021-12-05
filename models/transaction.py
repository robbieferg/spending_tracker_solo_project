from datetime import datetime


class Transaction:
    def __init__(self, date, time, amount_spent, merchant, tag, id = None, timestamp = None):
        self.date = date
        self.time = time
        self.amount_spent = amount_spent
        self.merchant = merchant
        self.tag = tag
        self.id = id


        datetime_string = f"{self.date} {self.time}"
        datetime_object = datetime.strptime(datetime_string, "%d/%m/%Y %H:%M")
        self.timestamp = datetime_object


        
