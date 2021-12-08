from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.budget import Budget
import repositories.budget_repository as budget_repository
from decimal import Decimal
import models.random_stat_generator as generator

budgets_blueprint = Blueprint("budgets", __name__)

@budgets_blueprint.route("/budgets")
def budgets():
    budgets = budget_repository.select_all()
    monthly_budget = round(Decimal(budgets[0].budget_amount), 2)
    stat = generator.get_random_stat()
    return render_template("budgets/budget.html", budget = monthly_budget, stat = stat)

@budgets_blueprint.route("/budgets", methods=['POST'])
def edit_budget():
    budgets = budget_repository.select_all()
    monthly_budget = budgets[0]
    budget_repository.update(monthly_budget, monthly_budget.budget_type, request.form['monthly_budget'])
    return redirect("/budgets")
