from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction

import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository

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

def get_monthly_average():
    months_passed_this_year = datetime.now().month
    all_transactions = transaction_repository.select_all()
    transactions_in_year = 0
    for transaction in all_transactions:
        if transaction.timestamp.year == datetime.now().year:
            transactions_in_year += transaction.amount_spent
    
    monthly_average = round((transactions_in_year / months_passed_this_year), 2)
    return monthly_average