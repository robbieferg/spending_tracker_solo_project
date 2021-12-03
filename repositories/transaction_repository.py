from db.run_sql import run_sql
from models.transaction import Transaction

def save(transaction):
    sql = "INSERT INTO transactions (date, amount_spent, merchant_id, tag_id) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [transaction.date, transaction.amount_spent, transaction.merchant.id, transaction.tag.id]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction

def update(transaction, new_date, new_amount_spent, new_merchant, new_tag):
    sql = "UPDATE transactions SET (date, amount_spent, merchant_id, tag_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = (new_date, new_amount_spent, new_merchant, new_tag, transaction.id)
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)