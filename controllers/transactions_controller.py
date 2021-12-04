from flask import Flask, render_template, request
from flask import Blueprint
from models.merchant import Merchant
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
from datetime import datetime

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    return render_template("transactions/index.html", transactions = transactions)

@transactions_blueprint.route("/transactions/add")
def add_transaction():
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    return render_template("transactions/add.html", merchants = merchants, tags = tags)