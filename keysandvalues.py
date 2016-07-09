# Есть набора данных в виде словаря

data = {
	'name': 'James',
	'second_name': 'Joyce',
	'birth': 1882,
	'born_at': 'Dublin',
	'death': 1941,
	'die_at': 'Zurich',
	'books': ['Ulysses', 'A Portrait of the Artist as a Young Man', 'Dubliners']
}

keys = list(data.keys())
values = list(data.values())

print(keys)
print(values)

#Returns list of dictionary dict's keys


# Нужно разработать алгоритм, который бы из одного словаря получил бы два списка:
#  в одном списке были бы только ключи (названия свойств словаря),
#  а в другом только значениях этих ключей,
#  называться эти списки должны соответственно keys и values
#
# Ожидается нечто подобное:
#    print(keys)
#    >>> ['name', 'second_name', 'birth', ... ]
#    print(values)
#    >>> ['James', 'Joyce', 1882, ...]
#
# Сделать это нужно автоматически, а еще лучше оформить в виде функции под названием decompose
