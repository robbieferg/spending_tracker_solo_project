from flask import Flask, render_template
from flask import Blueprint

from models import statistic_calculator as calculator


statistics_blueprint = Blueprint("statistics", __name__)

@statistics_blueprint.route("/statistics")
def show_statistics():
    total_this_year = '{:,}'.format(calculator.get_total_spend_current_year())
    average_per_month = '{:,}'.format(calculator.get_monthly_average_current_year())
    average_per_week = calculator.get_weekly_average_current_year()
    average_per_day = calculator.get_daily_average_current_year()

    return render_template("statistics/statistics.html", total_this_year = total_this_year, average_per_month = average_per_month, average_per_week = average_per_week, average_per_day = average_per_day)