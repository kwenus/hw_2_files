from pprint import pprint

from hw_2_ex_1 import cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    names = set()
    temp_dict = {}
    for dish in dishes:
        for item in cook_book[dish]:
            for key, value in dish.items():
                products.append([key, value])
            if item['ingredient_name'] in shop_list:


            else:
                shop_list[item['ingredient_name']] = {
                    'quantity': [item['quantity']],
                    'measure': item['measure'],
                }


    return shop_list

pprint(get_shop_list_by_dishes(['Нагетсы', 'Крылышки барбекю'], 3))

# if item['ingredient_name'] in shop_list:
#     shop_list[item['ingredient_name']] = {
#         'quantity': item['quantity'] + (item['quantity'] * person_count),
#         'measure': item['measure']
#     }
# else:
