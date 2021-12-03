from db.run_sql import run_sql
from models.merchant import Merchant

def save(merchant):
    sql = "INSERT INTO merchants(name, description) VALUES (%s, %s) RETURNING id"
    values = [merchant.name, merchant.description]
    results = run_sql(sql, values)
    merchant.id = results[0]['id']
    return merchant

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)

def update(merchant, name, description):
    sql = "UPDATE merchants SET (name, description) = (%s, %s) WHERE id = %s"
    values = [name, description, merchant.id]
    run_sql(sql, values)
    