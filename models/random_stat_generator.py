from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction
import models.total_spend_calculator as calculator

import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository

from datetime import datetime
import random

def generate_random_stat():
    stats_list = []

    months_passed_this_year = datetime.now().month
    all_transactions = transaction_repository.select_all()
    total_year_spend = calculator.total_spend(all_transactions)
    monthly_average = round((total_year_spend / months_passed_this_year), 2)
    monthly_average_string = f"Your monthly average spending for this year so far is £{monthly_average}"
    stats_list.append(monthly_average_string)

    current_datetime = datetime.today()
    weeks_passed_in_year = float(current_datetime.strftime("%V"))
    weekly_average = round((total_year_spend / weeks_passed_in_year), 2)
    weekly_average_string = f"Your weekly average spending for this year so far is £{weekly_average}"
    stats_list.append(weekly_average_string)

    all_tags = tag_repository.select_all()
    random_tag = random.choice(all_tags)
    random_tag_total_spend = 0
    for transaction in all_transactions:
        if transaction.tag.name == random_tag.name:
            random_tag_total_spend += transaction.amount_spent
    random_tag_spend_string = f"This year you have spent £{random_tag_total_spend} on {random_tag.name}."
    stats_list.append(random_tag_spend_string)

    all_merchants = merchant_repository.select_all()
    random_merchant = random.choice(all_merchants)
    random_merchant_total_spend = 0
    for transaction in all_transactions:
        if transaction.merchant.name == random_merchant.name:
            random_merchant_total_spend += transaction.amount_spent
    random_merchant_spend_string = f"This year you have spent £{random_merchant_total_spend} at {random_merchant.name}"
    stats_list.append(random_merchant_spend_string)

    return random.choice(stats_list)
    