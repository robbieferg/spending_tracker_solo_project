import pdb
from models.merchant import Merchant
from models.tag import Tag

import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

merchant_repository.delete_all()
tag_repository.delete_all()

merchant_1 = Merchant("Asda", "Supermarket")
merchant_repository.save(merchant_1)

merchant_2 = Merchant("OddBins", "Off License")
merchant_repository.save(merchant_2)

merchant_repository.update(merchant_1, "Ladbrokes", "Bookmaker")

tag_1 = Tag("Groceries")
tag_repository.save(tag_1)

tag_2 = Tag("Gambling")
tag_repository.save(tag_2)

tag_repository.update(tag_2, "Home Media")



pdb.set_trace()