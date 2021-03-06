from db.run_sql import run_sql
from models.transaction import Transaction
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

def save(transaction):
    sql = "INSERT INTO transactions (date, time, amount_spent, merchant_id, tag_id, timestamp) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [transaction.date, transaction.time, transaction.amount_spent, transaction.merchant.id, transaction.tag.id, transaction.timestamp]
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
        transaction = Transaction(row['date'], row['time'], row['amount_spent'], merchant, tag, row['id'], row['timestamp'])
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
        transaction = Transaction(result['date'], result['time'], result['amount_spent'], merchant, tag, result['id'], result['timestamp'])
    return transaction


def update(transaction, new_date, new_time, new_amount_spent, new_merchant, new_tag, new_timestamp):
    sql = "UPDATE transactions SET (date, time, amount_spent, merchant_id, tag_id, timestamp) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [new_date, new_time, new_amount_spent, new_merchant, new_tag, new_timestamp, transaction.id,]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)