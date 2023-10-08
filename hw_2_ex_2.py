from pprint import pprint

from hw_2_ex_1 import cook_book

# def get_shop_list_by_dishes(dishes, person_count):
#     shop_list = {}
#     for dish in dishes:
#         for el in cook_book[dish]:
#             if el['ingredient_name'] in shop_list:
#                 pass
#             else:
#                 shop_list[el['ingredient_name']] = {
#                     'measure': el['measure'],
#                     'quantity': el['quantity'] * person_count
#                 }
#     pprint(shop_list)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    list_products = []
    for dish in dishes:
        for el in cook_book[dish]:
            list_products.append(el['ingredient_name'])
            list_products.append(el['measure'])
            list_products.append(el['quantity'] * person_count)

    print(list_products)


get_shop_list_by_dishes(['Нагетсы'], 2)


