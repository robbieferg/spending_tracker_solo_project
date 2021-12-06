from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
from datetime import datetime
from operator import attrgetter
import models.total_spend_calculator as calculator

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    transactions_by_time = sorted(transactions, key=attrgetter('timestamp'))
    selected_view = "this year"
    
    total_spent = calculator.total_spend(transactions)
    month_spend = calculator.monthly_spend(transactions)
    
    
    return render_template("transactions/index.html", transactions_all = transactions, transactions_selected = transactions_by_time, total_spent = total_spent, selected_view = selected_view, month_spend = month_spend)

@transactions_blueprint.route("/transactions/add")
def add_transaction():
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    return render_template("transactions/add.html", merchants = merchants, tags = tags)

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
    return render_template("transactions/edit.html", transaction = transaction, merchants = merchants, tags = tags)

@transactions_blueprint.route("/transactions/<id>/edit", methods=['POST'])
def update_transaction(id):
    transaction = transaction_repository.select(id)
    merchant = merchant_repository.select_by_name(request.form['merchant'])
    tag = tag_repository.select_by_name(str(request.form['tag']))
    new_date = request.form['date']
    new_date = datetime.datetime.strptime(new_date, '%Y-%m-%d').strftime('%d/%m/%Y')
    transaction_repository.update(transaction, new_date, request.form['time'], request.form['amount_spent'], merchant.id, tag.id, transaction.timestamp)
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
    transaction_list = []
    for merchant in merchants_sorted:
        for transaction in transactions_by_time:
            if transaction.merchant.name == merchant.name:
                transaction_list.append(transaction)

    total_spent = calculator.total_spend(transactions)
    month_spend = calculator.monthly_spend(transactions)

    return render_template("transactions/index.html", transactions_all = transactions, transactions_selected = transaction_list, total_spent = total_spent, selected_view = selected_view, month_spend = month_spend)

@transactions_blueprint.route("/transactions/sort_by_tag")
def sort_by_tag():
    transactions = transaction_repository.select_all()
    transactions_by_time = sorted(transactions, key=attrgetter('timestamp'))
    tags = tag_repository.select_all()
    tags_sorted = sorted(tags, key=attrgetter('name'))
    selected_view = "this year"
    transaction_list = []
    for tag in tags_sorted:
        for transaction in transactions_by_time:
            if transaction.tag.name == tag.name:
                transaction_list.append(transaction)

    total_spent = calculator.total_spend(transactions)
    month_spend = calculator.monthly_spend(transactions)

    return render_template("transactions/index.html", transactions_all = transactions, transactions_selected = transaction_list, total_spent = total_spent, selected_view = selected_view, month_spend = month_spend)

@transactions_blueprint.route("/transactions/sort_by_date_time_reversed")
def sort_by_time_reversed():
    transactions = transaction_repository.select_all()
    selected_view = "this year"
    transactions_by_time = sorted(transactions, key=attrgetter('timestamp'))
    transactions_by_time.reverse()

    total_spent = calculator.total_spend(transactions)
    month_spend = calculator.monthly_spend(transactions)
    
    
    return render_template("transactions/index.html", transactions_all = transactions, transactions_selected = transactions_by_time, total_spent = total_spent, selected_view = selected_view, month_spend = month_spend)

@transactions_blueprint.route("/transactions/<month_name>/filter_month")
def filter_by_month(month_name):
    transactions = transaction_repository.select_all()
    selected_view = f"during {month_name}"
    transactions_by_month = []
    months = {"January" : "1", "February" : "2", "March" : "3", "April" : "4", "May" : "5", "June" : "6", "July" : "7", "August" : "8", "September" : "9", "October" : "10", "November" : "11", "December" : "12"}
    for transaction in transactions:
        month = transaction.timestamp.month
        
        if str(month) == months[month_name]:
            transactions_by_month.append(transaction)
    
    total_spent = calculator.total_spend(transactions_by_month)

    return render_template("transactions/index.html", transactions_all = transactions, transactions_selected = transactions_by_month, total_spent = total_spent, selected_view = selected_view)

@transactions_blueprint.route("/transactions/<merchant_name>/filter_merchant")
def filter_by_merchant(merchant_name):
    transactions = transaction_repository.select_all()
    selected_view = f"for {merchant_name}"
    transactions_by_merchant = []
    for transaction in transactions:
        if transaction.merchant.name == merchant_name:
            transactions_by_merchant.append(transaction)

    total_spent = calculator.total_spend(transactions_by_merchant)

    return render_template("transactions/index.html", transactions_all = transactions, transactions_selected = transactions_by_merchant, total_spent = total_spent, selected_view = selected_view)

@transactions_blueprint.route("/transactions/<tag_name>/filter_tag")
def filter_by_tag(tag_name):
    transactions = transaction_repository.select_all()
    selected_view = f"on {tag_name}"
    transactions_by_tag = []
    for transaction in transactions:
        if transaction.tag.name == tag_name:
            transactions_by_tag.append(transaction)

    total_spent = calculator.total_spend(transactions_by_tag)

    return render_template("transactions/index.html", transactions_all = transactions, transactions_selected = transactions_by_tag, total_spent = total_spent, selected_view = selected_view)