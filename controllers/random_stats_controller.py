from flask import Flask, render_template
from flask import Blueprint
import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
from models.merchant import Merchant
from models.transaction import Transaction
from decimal import Decimal

from models import statistic_calculator as calculator
import random


random_stats_blueprint = Blueprint("random_stats", __name__)

@random_stats_blueprint.route("/random_stats")
def show_statistics():
    stat_choices = []
    
    total_this_year = '{:,}'.format(calculator.get_total_spend_current_year())
    total_year_string = f"Your total expenditure this year is £{total_this_year}"
    stat_choices.append(total_year_string)


    average_per_month = '{:,}'.format(calculator.get_monthly_average_current_year())
    average_month_string = f"Your average monthly expenditure this year is £{average_per_month}"
    stat_choices.append(average_month_string)


    average_per_week = calculator.get_weekly_average_current_year()
    average_week_string = f"Your average weekly expenditure this year is £{average_per_week}"
    stat_choices.append(average_week_string)


    average_per_day = calculator.get_daily_average_current_year()
    average_day_string = f"Your average daily expenditure this year is £{average_per_day}"
    stat_choices.append(average_day_string)


    merchants_all = merchant_repository.select_all()
    random_merchant = random.choice(merchants_all)
    
    transactions_by_merchant = calculator.get_transactions_by_merchant(random_merchant.name)
    merchant_transactions_total = 0
    for transaction in transactions_by_merchant:
        merchant_transactions_total += transaction.amount_spent

    transactions_merchant_string = f"You have spent a total of £{merchant_transactions_total} at {random_merchant.name}"
    stat_choices.append(transactions_merchant_string)


    tags_all = tag_repository.select_all()
    random_tag = random.choice(tags_all)
    
    transactions_by_tag = calculator.get_transactions_by_tag(random_tag)
    tag_transactions_total = 0
    for transaction in transactions_by_tag:
        tag_transactions_total += transaction.amount_spent

    transactions_tag_string = f"You have spent a total of £{tag_transactions_total} on {random_tag.name}"
    stat_choices.append(transactions_tag_string)

    most_expensive_month = calculator.get_max_spend_month()
    transactions_of_month = calculator.get_transactions_by_month(most_expensive_month)
    cost_of_month = round(Decimal(calculator.get_total_spend(transactions_of_month)), 2)
    expensive_month_string = f"Your most expensive month this year was {most_expensive_month}, when you spent a total of £{cost_of_month}"
    stat_choices.append(expensive_month_string)



    stat_selected = random.choice(stat_choices)

    return render_template("random_stats/statistics.html", stat_selected = stat_selected)