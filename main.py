import os


# функция для форматирования ингредиентов
def set_of_tree_to_dict(*some_set):
    if len(some_set) == 3 and some_set[1].strip().isdigit():
        better_set = (some_set[0].strip(), int(some_set[1].strip()), some_set[2].strip())
        dict_names = ['ingredient_name', 'quantity', 'measure']
        output = dict(zip(dict_names, better_set))
        return output


# функция считывания с файла кулинарной книги
def get_cook_book_from_file(file_path):
    some_cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            entry = line.strip().split('|')
            if len(entry) == 1 and not entry[0].isdigit() and entry[0] != '':
                some_cook_book.setdefault(entry[0], [])
                amount_of_ingredients = int(f.readline().strip().split('|')[0])
                some_cook_book[entry[0]] = [set_of_tree_to_dict(*f.readline().strip().split('|')) for i in
                                       range(amount_of_ingredients)]

    return some_cook_book


# Задача №1 Считывание файла
file_path = 'flz/recipes.txt'
first_cook_book = get_cook_book_from_file(file_path)
print(f'Словарь кулинарной книги:')
for entry in first_cook_book.keys():
    print(f'{entry}:')
    [print(item) for item in first_cook_book[entry]]


# Задача №2 функция для списка блюд
def get_shop_list_by_dishes(dishes, person_count):
    pass


my_dishes = ['Запеченный картофель', 'Омлет', 'Фахитос']
my_persons_count = 2
