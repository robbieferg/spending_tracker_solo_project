from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction

import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository

from datetime import datetime

def get_total_spend(selected_transactions):
    total_spent = 0
    for transaction in selected_transactions:
        total_spent += float(transaction.amount_spent)
    total_spent = round(total_spent, 2)
    return total_spent

def get_monthly_spend(selected_transactions):
    monthly_spend = 0
    current_datetime = datetime.now()
    current_month = current_datetime.month
    for transaction in selected_transactions:
        if transaction.timestamp.month == current_month:
            monthly_spend += float(transaction.amount_spent)
    monthly_spend = round(monthly_spend, 2)
    return monthly_spend

def get_total_spend_current_year():
    all_transactions = transaction_repository.select_all()
    transactions_in_year = 0
    for transaction in all_transactions:
        if transaction.timestamp.year == datetime.now().year:
            transactions_in_year += transaction.amount_spent
    return transactions_in_year


def get_monthly_average_current_year():
    months_passed_this_year = datetime.now().month
    monthly_average = round((get_total_spend_current_year() / months_passed_this_year), 2)
    return monthly_average

def get_weekly_average_current_year():
    weeks_passed_in_year = float(datetime.now().strftime("%V"))
    weekly_average = round((float(get_total_spend_current_year()) / weeks_passed_in_year), 2)
    return weekly_average

def get_daily_average_current_year():
    days_passed_in_year = datetime.now().timetuple().tm_yday
    daily_average = round((float(get_total_spend_current_year()) / days_passed_in_year), 2)
    return daily_average

def get_transactions_by_month(month_name):
    transactions_all = transaction_repository.select_all()
    transactions_by_month = []
    months = {"January" : "1", "February" : "2", "March" : "3", "April" : "4", "May" : "5", "June" : "6", "July" : "7", "August" : "8", "September" : "9", "October" : "10", "November" : "11", "December" : "12"}
    for transaction in transactions_all:
        month = transaction.timestamp.month
        
        if str(month) == months[month_name]:
            transactions_by_month.append(transaction)

    return transactions_by_month

def get_transactions_by_merchant(merchant_name):
    transactions_all = transaction_repository.select_all()
    transactions_by_merchant = []
    for transaction in transactions_all:
        if transaction.merchant.name == merchant_name:
            transactions_by_merchant.append(transaction)

    return transactions_by_merchant

def get_transactions_by_tag(tag_name):
    transactions_all = transaction_repository.select_all()
    transactions_by_tag = []
    for transaction in transactions_all:
        if transaction.tag.name == tag_name:
            transactions_by_tag.append(transaction)
    return transactions_by_tag

def get_all_monthly_totals():
    all_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    months_passed = datetime.now().month
    spent_each_month = []

    if months_passed < 12:
        del all_months[months_passed:11]

    for month in all_months:
        month_transactions = get_transactions_by_month(month.capitalize())
        month_spend = get_total_spend(month_transactions)
        spent_each_month.append(month_spend)
    return spent_each_month
    
    
def get_max_spend_month():
    all_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    all_month_totals = get_all_monthly_totals()
    max_spend = max(all_month_totals)
    max_index = all_month_totals.index(max_spend)

    most_expensive_month = all_months[max_index]
    return most_expensive_month