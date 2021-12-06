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
        budgets.append(budget)
    return budgets

def select(budget_type):
    budget = None
    sql = "SELECT * FROM budgets WHERE budget_type = %s"
    values = [budget_type]
    result = run_sql(sql, values)[0]

    if result is not None:
        budget = Budget(result['budget_type'], result['budget_amount'], result['id'])
    return budget

def update(budget, new_budget_type, new_budget_amount):
    sql = "UPDATE budgets SET (budget_type, budget_amount) = (%s, %s) WHERE id = %s"
    values = [new_budget_type, new_budget_amount, budget.id]
    run_sql(sql, values)
