from collections import Counter


shop_list_1 = {
  'Соль': {'measure': 'ч.л', 'quantity': 1},
  'Помидор': {'measure': 'шт', 'quantity': 4},
  'Специи': {'measure': 'шт', 'quantity': 1}
}
shop_list_2 = {
  'Сыр гауда': {'measure': 'г', 'quantity': 200},
  'Соль': {'measure': 'ч.л', 'quantity': 2},
  'Специи': {'measure': 'шт', 'quantity': 2}
}

dishes = [shop_list_2, shop_list_1]
products =[]

for dish in dishes:
  for key, value in dish.items():
    products.append([key, value])
# print(products)

shop_list ={}
names = set()
quant = {}
for key, item in products:
  if key in names:
    shop_list[key]['quantity'] += quant[key]   # добавляем количество из уникального словаря
  else:
    shop_list[key] = item
    names.add(key)                      # сохраняем список названий
    quant[key] = item['quantity']       # делаем словарь из уникальных значений (название: количество)
print(shop_list)
# print(shop_list)

# print(shop_list_2.values())
# print(shop_list_2.keys())
# print(shop_list_2.items())

# shop_list_2.setdefault(shop_list_1)

# print('Соль' in shop_list_2)
#
# dict_values([{'measure': 'г', 'quantity': 200}, {'measure': 'ч.л', 'quantity': 2}])
# dict_keys(['Сыр гауда', 'Соль'])
# dict_items([('Сыр гауда', {'measure': 'г', 'quantity': 200}), ('Соль', {'measure': 'ч.л', 'quantity': 2})])
# # print(shop_list_1['Соль']['quantity'] + shop_list_1['Соль']['quantity'])
#
# shop_list_2.update(['Соль'], 3)
# # print(shop_list_1)
# print(shop_list_2)

