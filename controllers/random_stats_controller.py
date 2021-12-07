from os import stat
from flask import Flask, render_template
from flask import Blueprint
import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
from models.merchant import Merchant
from models.transaction import Transaction
from decimal import Decimal

from models import statistic_calculator as calculator
from models import random_stat_generator as generator
import random


random_stats_blueprint = Blueprint("random_stats", __name__)

@random_stats_blueprint.route("/random_stats")
def show_statistics():
    stat_selected = random.choice(generator.all_functions)()

    return render_template("random_stats/statistics.html", stat_selected = stat_selected)