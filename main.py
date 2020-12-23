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


# функция для составления списка покупок
def get_shop_list_by_dishes(person_count, cook_book, *dishes):
    # список ингредиентов с повторениями
    all_dishes = ['spam']
    shopping_list = {}
    for dish in dishes:
        all_dishes += [{unit.pop('ingredient_name'): unit} for unit in cook_book[dish] if dish in cook_book.keys()]
    all_dishes.pop(0)

    # список ингредиентов без повторений
    # мне кажется, добжен быть способ слияния словарей, но я его не нашёл
    for entry in all_dishes:
        if shopping_list.get(list(entry.keys())[0]) is not None:
            shopping_list[list(entry.keys())[0]]['quantity'] += list(entry.values())[0]['quantity'] * person_count
        else:
            shopping_list[list(entry.keys())[0]] = list(entry.values())[0]
            shopping_list[list(entry.keys())[0]]['quantity'] = list(entry.values())[0]['quantity'] * person_count

    return shopping_list


# Задача №1 Считывание файла
my_file_path = 'flz/recipes.txt'
my_cook_book = get_cook_book_from_file(my_file_path)
print(f'Словарь кулинарной книги:')
for entry in my_cook_book.keys():
    print(f'{entry}:')
    [print(item) for item in my_cook_book[entry]]


# Задача №2 Список покупок
my_dishes = ['Омлет', 'Фахитос']
my_persons_count = 3
my_shopping_list = get_shop_list_by_dishes(my_persons_count, my_cook_book, *my_dishes)
print(f'\nДля приготовления {", ".join(my_dishes)} на {my_persons_count} человека необходимо купить:')
for entry in my_shopping_list:
         print(f'{entry} : {my_shopping_list[entry]["quantity"]} {my_shopping_list[entry]["measure"]}')