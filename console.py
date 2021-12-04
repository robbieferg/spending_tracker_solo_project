import pdb
from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction

import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository

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


transaction_1 = Transaction("04/12/2021", 12.50, merchant_1, tag_2)
transaction_repository.save(transaction_1)
transaction_2 = Transaction("11/11/2021", 35.75, merchant_3, tag_3)
transaction_repository.save(transaction_2)




pdb.set_trace()