from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction

import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository

random_stats_blueprint = Blueprint("random_stats", __name__)

@random_stats_blueprint.route("/random_stats")
def show_random_stat():
    return render_template("random_stats/random_stat.html")