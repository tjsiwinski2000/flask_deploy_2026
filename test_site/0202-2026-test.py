from get_user_data_from_db import get_user_data_db
from get_shop_data_from_db import get_coffee_shops
s= get_user_data_db(filter = 'tjsiwinski')
print(s)
print(type(s))
print(s[0]['password'])

# s= get_coffee_shops(filter = 'all')
# print(s)