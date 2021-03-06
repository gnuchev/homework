# Нужно написать несколько функций

# 1) функция remove
# Эта функция удаляет из списка элемент с данным индексом

lst = []

def remove(lst, index):
    try:
	#pass
    #lst = []
        del lst[index]
    except IndexError:
            return print(lst)
        #if index not in lst:
        #    print('no index')
        #else:
        
    return print(lst)

# пример использования:

remove(['a', 'b', 'c'], 1) # Ожидается: ['a', 'c']
remove([1, 2, 3, 4, 5], 0) # Ожидается: [2, 3, 4, 5]
remove([1, 2, 3, 3, 4], 10) # Ожидается: [1, 2, 3, 4, 5]

# Если в списке нет элемента за данным индексом, то делать ничего не надо

# 2) Функция reverse
# Эта функция переворачивает список

lst = []

def reverse(lst):
    lst.reverse()
    return print(lst)

# пример использования:

reverse(['a', 'b', 'c']) # Ожидается: ['c', 'b', 'a']
reverse([1, 2, 3]) # Ожидается: [3, 2, 1]


'''
# Сложные версии:

# 3) Функция omit
# Эта функция вырезает из первого аргумента (словарь), все ключи из списка второго аргумента

def omit(hash, lst):
	pass

# пример использования

data = {
	'name': 'John',
	'second_name': 'Doe',
	'age': 28
}

omit(data, ['age']) # Ожидается словарь похожий на data, но без ключа 'age' {'name': 'John', 'second_name': 'Doe'}
omit(data, ['name', 'second_name']) # Ожидается: {'age': 27}
omit(data, ['unknown']) # Ожидается тот же словарь, что и на входе, т.к. ключа 'unknown' в нем нет, то и вырезать ничего не надо

# Подсазка

# Чтобы узнать, если ли ключ в словаре, используйте оператор in
'a' in {'a': 10} # - это True
'b' in {'a': 10} # - это False
'''
