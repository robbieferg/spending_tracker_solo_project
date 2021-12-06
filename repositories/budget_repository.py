from db.run_sql import run_sql
from models.budget import Budget

def save(budget):
    sql = "INSERT INTO budgets (budget_type, budget_amount) VALUES (%s, %s) RETURNING id"
    values = [budget.budget_type, budget.budget_amount]
    results = run_sql(sql, values)
    budget.id = results[0]['id']
    return budget

def select_all():
    budgets = []
    sql = "SELECT * FROM budgets"
    results = run_sql(sql)
    for row in results:
        budget = Budget(row['budget_type'], row['budget_amount'], row['id'])
        budgets.append(tag)
    return budgets

def update(budget, new_budget_type, new_budget_amount):
    sql = "UPDATE budgets SET (budget_type, budget_amount) = (%s, %s) WHERE id = %s"
    values = [new_budget_type, new_budget_amount, budget.id]
    run_sql(sql, values)
