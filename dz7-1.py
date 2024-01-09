import os
import pickle
import json

fe = 'orders_pik09.txt'
history_file = 'purchase_history.json'

# Инициализация счета и истории покупок
total_cost = 0
purchase_history = []

# Загрузка данных из файлов, если они существуют
if os.path.exists(fe):
    with open(fe, 'rb') as f:
        data = pickle.load(f)
        orders = data['orders']
        total_cost = data['total_cost']

if os.path.exists(history_file):
    with open(history_file, 'r') as f:
        purchase_history = json.load(f)

while True:
    print('1. Добавить покупку')
    print("2. История покупок")
    print("3. Показать сумму счета")
    print("4. Просмотр содержимого рабочей директории")
    print("5. Сохранить содержимое рабочей директории в файл")
    print("6. Выход")
    choice = input("Введите номер действия: ")

    if choice == '1':
        name = input('Введите название товара: ')
        try:
            cost = float(input('Введите цену товара: '))
            order = (name, cost)
            orders.append(order)
            total_cost += cost
            print(f'Товар "{name}" с ценой {cost} успешно добавлен.')

            # Добавление покупки в историю
            purchase_history.append({"name": name, "cost": cost})

        except ValueError:
            print('Ошибка: Введите корректное число для цены.')

    elif choice == '2':
        if purchase_history:
            print('История покупок:')
            for purchase in purchase_history:
                print(f'Товар: {purchase["name"]}, Цена: {purchase["cost"]}')
        else:
            print('История покупок пуста.')

    elif choice == '3':
        print(f'Сумма счета: {total_cost}')

    elif choice == '4':
        # Просмотр содержимого рабочей директории
        current_directory = os.getcwd()
        print(f"Содержимое рабочей директории {current_directory}:")
        for item in os.listdir(current_directory):
            print(item)

    elif choice == '5':
        # Сохранение содержимого рабочей директории в файл
        current_directory = os.getcwd()
        files = []
        dirs = []

        for item in os.listdir(current_directory):
            if os.path.isfile(item):
                files.append(item)
            elif os.path.isdir(item):
                dirs.append(item)

        with open('listdir.txt', 'w') as f:
            f.write(f'files: {", ".join(files)}\n')
            f.write(f'dirs: {", ".join(dirs)}\n')
        print('Содержимое рабочей директории сохранено в файл listdir.txt.')

    elif choice == '6':
        # Сохранение данных перед выходом
        with open(fe, 'wb') as f:
            data = {'orders': orders, 'total_cost': total_cost}
            pickle.dump(data, f)

        # Сохранение истории покупок в JSON файле
        with open(history_file, 'w') as f:
            json.dump(purchase_history, f)

        break

    else:
        print('Неверный формат ввода. Введите номер действия от 1 до 6.')
