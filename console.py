import pdb
from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction
from models.budget import Budget
from datetime import datetime

import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository
import repositories.budget_repository as budget_repository

transaction_repository.delete_all()
merchant_repository.delete_all()
tag_repository.delete_all()

merchant_1 = Merchant("Asda", "Supermarket")
merchant_repository.save(merchant_1)

merchant_2 = Merchant("OddBins", "Off License")
merchant_repository.save(merchant_2)

merchant_3 = Merchant("Amazon", "Online Superstore")
merchant_repository.save(merchant_3)


tag_1 = Tag("Groceries")
tag_repository.save(tag_1)

tag_2 = Tag("Gambling")
tag_repository.save(tag_2)

tag_3 = Tag("Gaming")
tag_repository.save(tag_3)


transaction_1 = Transaction("04/12/2021", "15:35", 12.50, merchant_1, tag_2)
transaction_repository.save(transaction_1)
transaction_2 = Transaction("11/11/2021", "15:35", 35.75, merchant_3, tag_3)
transaction_repository.save(transaction_2)

month = transaction_1.timestamp.month
print(month)

budget_1 = Budget("monthly", 350.00)
budget_repository.save(budget_1)






pdb.set_trace()