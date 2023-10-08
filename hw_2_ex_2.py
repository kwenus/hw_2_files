from pprint import pprint

from hw_2_ex_1 import cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    list_products = []                         # создаем список продуктов
    for dish in dishes:                        # выбираем блюдо в списке
        for recipe in cook_book[dish]:         # выбираем рецепт по названию блюда
            ingridient = []                    # создаем пустой ингридиенто
            for item in recipe.items():        # получаем элемент списка через метод items
                ingridient.append(item[1])     # добавляем элемент в ингридиент
            list_products.append(ingridient)   # добавляем ингридиент в список продуктов

    for element in list_products:
        element[1] = element[1] * person_count


    pprint(sorted(list_products))


get_shop_list_by_dishes(['Запеченный картофель', 'Уха', 'Нагетсы', 'Омлет'], 3)


