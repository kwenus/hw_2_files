from pprint import pprint

from hw_2_ex_1 import cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for item in cook_book[dish]:
            shop_list[item['ingredient_name']] = {
                'quantity': item['quantity'] * person_count,
                'measure': item['measure']
            }
    return shop_list

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Уха'], 3))

