from pprint import pprint

# считываем информацию из файла:

with open('recipes.txt') as recipes:
    string_of_recipes = recipes.read()

# создаем список рецептов без лишних символов:
recipes_list = string_of_recipes.split('\n')

# создаем список с отдельными рецептами для доступа по индексу:
sep_recipes = []
while recipes_list:
    recipe = []
    for el in recipes_list:
        if el == '':
            recipe.append(el)
            sep_recipes.append(recipe)
            for ingr in recipe:
                if ingr in recipes_list:
                    recipes_list.remove(ingr)
            break
        else:
            recipe.append(el)

# создаем книгу рецептов

cook_book = {}

for el in sep_recipes:
    cook_book[el[0]] = [{'ingredient_name': (el[2+id].split('|')[0]).strip(), 'quantity': int(el[2+id].split('|')[1]),
                        'measure': (el[2+id].split('|')[2]).strip()} for id, loop in enumerate(range(int(el[1])))]

# pprint(cook_book)
