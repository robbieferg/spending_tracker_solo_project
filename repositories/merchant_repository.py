from db.run_sql import run_sql
from models.merchant import Merchant

def save(merchant):
    sql = "INSERT INTO merchants(name, description) VALUES (%s, %s) RETURNING id"
    values = [merchant.name, merchant.description]
    results = run_sql(sql, values)
    merchant.id = results[0]['id']
    return merchant

def select_all():
    merchants = []

    sql = "SELECT * FROM merchants"
    results = run_sql(sql)
    for row in results:
        merchant = Merchant(row['name'], row['description'], row['active'], row['id'])
        merchants.append(merchant)
    return merchants

def select(id):
    merchant = None
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        merchant = Merchant(result['name'], result['description'], result['active'], result['id'])
    return merchant

def select_by_name(name):
    merchant = None
    sql = "SELECT * FROM merchants WHERE name = %s"
    values = [name]
    result = run_sql(sql, values)[0]

    if result is not None:
        merchant = Merchant(result['name'], result['description'], result['active'], result['id'])
    return merchant

def update(merchant, new_name, new_description, new_active):
    sql = "UPDATE merchants SET (name, description, active) = (%s, %s, %s, %s) WHERE id = %s"
    values = [new_name, new_description, new_active, merchant.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)


    