from typing import Generator
import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
from models.merchant import Merchant
from models.transaction import Transaction
from decimal import Decimal

from models import statistic_calculator as calculator
import random

def get_total_spend_current_year_stat():
    
    total_this_year = '{:,}'.format(calculator.get_total_spend_current_year())
    total_year_string = f"Your total expenditure this year is £{total_this_year}"
    return total_year_string

def get_average_spend_per_month_stat():
    average_per_month = '{:,}'.format(calculator.get_monthly_average_current_year())
    average_month_string = f"Your average monthly expenditure this year is £{average_per_month}"
    return average_month_string

def get_weekly_average_stat():
    average_per_week = calculator.get_weekly_average_current_year()
    average_week_string = f"Your average weekly expenditure this year is £{average_per_week}"
    return average_week_string

def get_daily_average_stat():
    average_per_day = calculator.get_daily_average_current_year()
    average_day_string = f"Your average daily expenditure this year is £{average_per_day}"
    return average_day_string

def get_total_for_merchant_stat():
    merchants_all = merchant_repository.select_all()
    random_merchant = random.choice(merchants_all)
    
    transactions_by_merchant = calculator.get_transactions_by_merchant(random_merchant.name)
    merchant_transactions_total = 0
    for transaction in transactions_by_merchant:
        merchant_transactions_total += transaction.amount_spent

    transactions_merchant_string = f"You have spent a total of £{merchant_transactions_total} at {random_merchant.name}"
    return transactions_merchant_string

def get_total_for_tag_stat():
    tags_all = tag_repository.select_all()
    random_tag = random.choice(tags_all)
    
    transactions_by_tag = calculator.get_transactions_by_tag(random_tag)
    tag_transactions_total = 0
    for transaction in transactions_by_tag:
        tag_transactions_total += transaction.amount_spent

    transactions_tag_string = f"You have spent a total of £{tag_transactions_total} on {random_tag.name}"
    return transactions_tag_string

def get_most_expensive_month_stat():
    most_expensive_month = calculator.get_max_spend_month()
    transactions_of_month = calculator.get_transactions_by_month(most_expensive_month)
    cost_of_month = round(Decimal(calculator.get_total_spend(transactions_of_month)), 2)
    expensive_month_string = f"Your most expensive month this year was {most_expensive_month}, when you spent a total of £{cost_of_month}"
    return expensive_month_string

def get_least_expensive_month_stat():
    least_expensive_month = calculator.get_min_spend_month()
    transactions_min_month = calculator.get_transactions_by_month(least_expensive_month)
    cost_min_month = round(Decimal(calculator.get_total_spend(transactions_min_month)), 2)
    least_expensive_month_string = f"Your least expensive month this year was {least_expensive_month}, when you spent £{cost_min_month}"
    return least_expensive_month_string

def get_most_popular_merchant_stat():
    most_popular_merchant = calculator.get_most_popular_merchant()
    popular_merchant_transactions = calculator.get_transactions_by_merchant(most_popular_merchant)
    popular_merchant_total = calculator.get_total_spend(popular_merchant_transactions)
    most_popular_merchant_string = f"Your favourite merchant is {most_popular_merchant}. You have spent £{popular_merchant_total} at this merchant."
    return most_popular_merchant_string

def get_most_popular_tag_stat():
    most_popular_tag = calculator.get_most_popular_tag()
    popular_tag_transactions = calculator.get_transactions_by_tag(most_popular_tag)
    popular_tag_total = calculator.get_total_spend(popular_tag_transactions)
    most_popular_tag_string = f"Your favourite tag is {most_popular_tag}. You have spent £{popular_tag_total} on transactions with this tag."

all_functions = [get_total_spend_current_year_stat, get_average_spend_per_month_stat, get_weekly_average_stat, get_daily_average_stat, get_total_for_merchant_stat, get_total_for_tag_stat, get_most_expensive_month_stat, get_most_expensive_month_stat, get_least_expensive_month_stat, get_least_expensive_month_stat, get_most_popular_merchant_stat, get_most_popular_merchant_stat]




