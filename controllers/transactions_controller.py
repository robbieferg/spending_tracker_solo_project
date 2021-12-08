from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.budget_repository as budget_repository
from datetime import datetime
from operator import attrgetter
import models.statistic_calculator as calculator
import models.random_stat_generator as generator

from decimal import Decimal

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    transactions_by_time = sorted(transactions, key=attrgetter('timestamp'))
    selected_view = "this year"
    monthly_budget = Decimal(budget_repository.select("monthly").budget_amount)
    monthly_budget = round(monthly_budget, 2)
    
    total_spent = Decimal(calculator.get_total_spend(transactions))
    total_spent = round(total_spent, 2)
    month_spend = Decimal(calculator.get_monthly_spend(transactions))
    month_spend = round(month_spend, 2)
    
    
    return render_template("transactions/index.html", transactions_all = transactions, transactions_selected = transactions_by_time, total_spent = total_spent, selected_view = selected_view, month_spend = month_spend, monthly_budget = monthly_budget)

@transactions_blueprint.route("/transactions/add")
def add_transaction():
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    stat = generator.get_random_stat()
    return render_template("transactions/add.html", merchants = merchants, tags = tags, stat = stat)

@transactions_blueprint.route("/transactions/add", methods=['POST'])
def new_transaction():
    date = str(request.form['date'])
    date = datetime.strptime(date, '%Y-%m-%d').strftime('%d/%m/%Y')
    time = str(request.form['time'])
    amount_spent = request.form['amount_spent']
    merchant = merchant_repository.select_by_name(request.form['merchant'])
    tag = tag_repository.select_by_name(request.form['tag'])
    transaction = Transaction(date, time, amount_spent, merchant, tag)
    transaction_repository.save(transaction)
    return redirect("/transactions")

@transactions_blueprint.route("/transactions/<id>/edit")
def edit_transaction(id):
    transaction = transaction_repository.select(id)
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    date_string = datetime.strptime(transaction.date, "%d/%m/%Y").strftime("%Y-%m-%d")
    stat = generator.get_random_stat()
    return render_template("transactions/edit.html", transaction = transaction, merchants = merchants, tags = tags, date_string = date_string, stat = stat)

@transactions_blueprint.route("/transactions/<id>/edit", methods=['POST'])
def update_transaction(id):
    transaction = transaction_repository.select(id)
    merchant = merchant_repository.select_by_name(request.form['merchant'])
    tag = tag_repository.select_by_name(str(request.form['tag']))
    new_date = str(request.form['date'])
    new_date = datetime.strptime(new_date, '%Y-%m-%d').strftime('%d/%m/%Y')
    new_time = str(request.form['time'])
    datetime_string = f"{new_date} {new_time}"
    datetime_object = datetime.strptime(datetime_string, "%d/%m/%Y %H:%M")
    new_timestamp = datetime_object
    transaction_repository.update(transaction, new_date, new_time, request.form['amount_spent'], merchant.id, tag.id, new_timestamp)
    return redirect("/transactions")

@transactions_blueprint.route("/transactions/<id>/delete")
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect("/transactions")

@transactions_blueprint.route("/transactions/sort_by_merchant")
def sort_by_merchant():
    transactions = transaction_repository.select_all()
    transactions_by_time = sorted(transactions, key=attrgetter('timestamp'))
    merchants = merchant_repository.select_all()
    merchants_sorted = sorted(merchants, key=attrgetter('name'))
    selected_view = "this year"
    monthly_budget = budget_repository.select("monthly").budget_amount
    transaction_list = []
    for merchant in merchants_sorted:
        for transaction in transactions_by_time:
            if transaction.merchant.name == merchant.name:
                transaction_list.append(transaction)

    total_spent = calculator.get_total_spend(transactions)
    month_spend = calculator.get_monthly_spend(transactions)

    return render_template("transactions/index.html", transactions_all = transactions, transactions_selected = transaction_list, total_spent = total_spent, selected_view = selected_view, month_spend = month_spend, monthly_budget = monthly_budget)

@transactions_blueprint.route("/transactions/sort_by_tag")
def sort_by_tag():
    transactions = transaction_repository.select_all()
    transactions_by_time = sorted(transactions, key=attrgetter('timestamp'))
    tags = tag_repository.select_all()
    tags_sorted = sorted(tags, key=attrgetter('name'))
    selected_view = "this year"
    monthly_budget = budget_repository.select("monthly").budget_amount
    transaction_list = []
    for tag in tags_sorted:
        for transaction in transactions_by_time:
            if transaction.tag.name == tag.name:
                transaction_list.append(transaction)

    total_spent = calculator.get_total_spend(transactions)
    month_spend = calculator.get_monthly_spend(transactions)

    return render_template("transactions/index.html", transactions_all = transactions, transactions_selected = transaction_list, total_spent = total_spent, selected_view = selected_view, month_spend = month_spend, monthly_budget = monthly_budget)

@transactions_blueprint.route("/transactions/sort_by_date_time_reversed")
def sort_by_time_reversed():
    transactions = transaction_repository.select_all()
    selected_view = "this year"
    monthly_budget = budget_repository.select("monthly").budget_amount
    transactions_by_time = sorted(transactions, key=attrgetter('timestamp'))
    transactions_by_time.reverse()

    total_spent = calculator.get_total_spend(transactions)
    month_spend = calculator.get_monthly_spend(transactions)
    
    
    return render_template("transactions/index.html", transactions_all = transactions, transactions_selected = transactions_by_time, total_spent = total_spent, selected_view = selected_view, month_spend = month_spend, monthly_budget = monthly_budget)

@transactions_blueprint.route("/transactions/<month_name>/filter_month")
def filter_by_month(month_name):
    transactions = transaction_repository.select_all()
    selected_view = f"during {month_name}"
    transactions_by_month = calculator.get_transactions_by_month(month_name)
    
    total_spent = round(Decimal(calculator.get_total_spend(transactions_by_month)), 2)

    return render_template("transactions/index.html", transactions_all = transactions, transactions_selected = transactions_by_month, total_spent = total_spent, selected_view = selected_view)

@transactions_blueprint.route("/transactions/<merchant_name>/filter_merchant")
def filter_by_merchant(merchant_name):
    transactions = transaction_repository.select_all()
    selected_view = f"for {merchant_name}"
    transactions_by_merchant = calculator.get_transactions_by_merchant(merchant_name)

    total_spent = round(Decimal(calculator.get_total_spend(transactions_by_merchant)), 2)

    return render_template("transactions/index.html", transactions_all = transactions, transactions_selected = transactions_by_merchant, total_spent = total_spent, selected_view = selected_view)

@transactions_blueprint.route("/transactions/<tag_name>/filter_tag")
def filter_by_tag(tag_name):
    transactions = transaction_repository.select_all()
    selected_view = f"on {tag_name}"
    transactions_by_tag = calculator.get_transactions_by_tag(tag_name)

    total_spent = round(Decimal(calculator.get_total_spend(transactions_by_tag)), 2)

    return render_template("transactions/index.html", transactions_all = transactions, transactions_selected = transactions_by_tag, total_spent = total_spent, selected_view = selected_view)