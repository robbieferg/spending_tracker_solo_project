from flask import Flask, render_template
from flask import Blueprint

from models import statistic_calculator as calculator


statistics_blueprint = Blueprint("statistics", __name__)

@statistics_blueprint.route("/random_stats")
def show_random_stat():
    output = calculator.get_monthly_average()
    return render_template("statistics/statistics.html", output = output)