# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
# Функция stud_counter() возвращает словарь с именами и числом их повторений


def stud_counter(students):
    stud_list = []
    result = {}
    for list_items in students:
        stud_list.append(list_items.get('first_name', ''))
    for name in set(stud_list):
        result[name] = stud_list.count(name)
    return result


for name, count in stud_counter(students).items():
    print(f'{name} : {count}')

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]


def main_name(students):
    max_stud = 0
    for name, count in stud_counter(students).items():
        if count > max_stud:
            max_stud = count
            stud_name = name
    return stud_name


print(f'Самое частое имя среди учеников: {main_name(students)}')


# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ]
]

for i in range(len(school_students)):
    print(f'Самое частое имя в классе {i+1}: {main_name(school_students[i])}')

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
    {'class': '2a', 'students': [
        {'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [
        {'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

# Данная функция возвращает новый список с информацией о колличестве мальчиков
# и девочек в каждом классе


def new_counter(school_list, is_male_dict):
    new_school_list = []
    for class_n in school_list:
        boys = 0
        girls = 0
        for stud in class_n['students']:
            stud_name = stud.get('first_name')
            if is_male_dict[stud_name]:
                boys += 1
            else:
                girls += 1
        new_school_list.append(
            {'class': class_n['class'], 'boys': boys, 'girls': girls})
    return new_school_list


for cl in new_counter(school, is_male):
    # не работает :
    # print(f'В классе {cl.get('class')} : {cl.get('boys')} мальчиков и {cl.get('girls')} девочек')
    class_name = cl.get('class')
    boys_num = cl.get('boys')
    girls_num = cl.get('girls')
    print(f'В классе {class_name}: {boys_num} мальчиков и {girls_num} девочек')


# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
    {'class': '2a', 'students': [
        {'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [
        {'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

boys = 0
girls = 0
for cl in new_counter(school, is_male):

    class_name = cl.get('class')
    boys_num = cl.get('boys')
    girls_num = cl.get('girls')
    if boys_num > boys:
        boys += boys_num
        boys_class = class_name
    if girls_num > girls:
        girls += girls_num
        girls_class = class_name

print(f'Больше всего мальчиков в классе {boys_class}')
print(f'Больше всего девочек в классе {girls_class}')

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
