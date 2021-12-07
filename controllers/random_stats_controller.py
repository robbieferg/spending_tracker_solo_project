from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models import random_stat_generator


random_stats_blueprint = Blueprint("random_stats", __name__)

@random_stats_blueprint.route("/random_stats")
def show_random_stat():
    output = random_stat_generator.generate_random_stat()
    return render_template("random_stats/random_stat.html", output = output)