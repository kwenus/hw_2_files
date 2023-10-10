from pprint import pprint

from hw_2_ex_1_v2 import cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}                                                                                                      # создаем список покупок
    for dish in dishes:
        for item in cook_book[dish]:
            if item['ingredient_name'] in shop_list:                                                                    # если продукт уже в списке покупок изменяем
                shop_list[item['ingredient_name']]['quantity'] += (item['quantity'] * person_count)                     # его значение по ключу
            else:
                shop_list[item['ingredient_name']] = {                                                                  # если нет заполняем значения по ключам
                    'quantity': item['quantity'] * person_count,
                    'measure': item['measure'],
                }
    return shop_list

pprint(get_shop_list_by_dishes(['Нагетсы', 'Крылышки барбекю', 'Омлет'], 3))
