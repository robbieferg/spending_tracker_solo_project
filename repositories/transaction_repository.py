from db.run_sql import run_sql
from models.transaction import Transaction
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

def save(transaction):
    sql = "INSERT INTO transactions (date, amount_spent, merchant_id, tag_id) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [transaction.date, transaction.amount_spent, transaction.merchant.id, transaction.tag.id]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction

def select_all():
    transactions = []
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    for row in results:
        merchant = merchant_repository.select(row['merchant_id'])
        tag = tag_repository.select(row['tag_id'])
        transaction = Transaction(row['date'], row['amount_spent'], merchant, tag, row['id'])
        transactions.append(transaction)
    return transactions

def select(id):
    transaction = None
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        merchant = merchant_repository.select(result['merchant_id'])
        tag = tag_repository.select(result['tag_id'])
        transaction = Transaction(result['date'], result['amount_spent'], merchant, tag, result['id'])
    return transaction


def update(transaction, new_date, new_amount_spent, new_merchant, new_tag):
    sql = "UPDATE transactions SET (date, amount_spent, merchant_id, tag_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = (new_date, new_amount_spent, new_merchant, new_tag, transaction.id)
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)