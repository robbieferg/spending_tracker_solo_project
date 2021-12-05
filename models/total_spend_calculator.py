def total_spend(selected_transactions):
    total_spent = 0
    for transaction in selected_transactions:
        total_spent += float(transaction.amount_spent)
    total_spent = "{:,}".format(round(total_spent, 2))
    return total_spent