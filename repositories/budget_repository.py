from db.run_sql import run_sql
from models.tag import Tag

def save(budget):
    sql = "INSERT INTO budgets (budget_type, budget_amount) VALUES (%s, %s) RETURNING id"
    values = [budget.budget_type, budget.budget_amount]
    results = run_sql(sql, values)
    budget.id = results[0]['id']
    return budget