from datetime import datetime

def total_spend(selected_transactions):
    total_spent = 0
    for transaction in selected_transactions:
        total_spent += float(transaction.amount_spent)
    total_spent = round(total_spent, 2)
    return total_spent

def monthly_spend(selected_transactions):
    monthly_spend = 0
    current_datetime = datetime.now()
    current_month = current_datetime.month
    for transaction in selected_transactions:
        if transaction.timestamp.month == current_month:
            monthly_spend += float(transaction.amount_spent)
    monthly_spend = round(monthly_spend, 2)
    return monthly_spend
