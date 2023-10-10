# считываение файла построчно,
# с добавлением маркера конца файла
# (не нашел как это сделать по другому)

from pprint import pprint


with open('recipes.txt') as recipes:
    sep_recipes = []
    line = ''
    while line != 'end':
        recipe = []
        for line in recipes:
            if line == '\n':
                sep_recipes.append(recipe)
                break
            else:
                recipe.append(line.strip('\n'))

    cook_book = {}
    for el in sep_recipes:
        cook_book[el[0]] = [
            {'ingredient_name': (el[2 + id].split('|')[0]).strip(), 'quantity': int(el[2 + id].split('|')[1]),
             'measure': (el[2 + id].split('|')[2]).strip()} for id, loop in enumerate(range(int(el[1])))]
pprint(cook_book)