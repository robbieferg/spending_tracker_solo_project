from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import datetime
from operator import attrgetter

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    transactions_by_time = sorted(transactions, key=attrgetter('timestamp'))
    
    total_spent = 0
    for transaction in transactions:
        total_spent += float(transaction.amount_spent)
    total_spent = "{:,}".format(round(total_spent, 2))
    
    
    return render_template("transactions/index.html", transactions = transactions_by_time, total_spent = total_spent)

@transactions_blueprint.route("/transactions/add")
def add_transaction():
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    return render_template("transactions/add.html", merchants = merchants, tags = tags)

@transactions_blueprint.route("/transactions/add", methods=['POST'])
def new_transaction():
    date = str(request.form['date'])
    date = datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%d/%m/%Y')
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
    transaction_list = []
    for merchant in merchants_sorted:
        for transaction in transactions_by_time:
            if transaction.merchant.name == merchant.name:
                transaction_list.append(transaction)

    return render_template("transactions/index.html", transactions = transaction_list)