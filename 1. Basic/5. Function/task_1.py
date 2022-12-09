documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def people():
    '''Выводим имя человека по номеру документа.'''
    document = input('Введите номер документа: ')
    for doc in documents:
        if document == doc['number']:
            name = doc['name']
            print(f'Владелец документа: {name}')
            return
    print('Документ по заданному номеру не найден!')


def shelf():
    '''Выводим номер полки на которой находится запрашиваемый документ.'''
    document = input('Введите номер документа: ')
    for key, value in directories.items():
        if document in value:
            print(f'Документ "{document}" находится на полке: №{key}')
            return
    print('Для поиска номера полки, номер документа указан неверно!')


def doc_list():
    '''Вывод информации всех документов.'''
    for doc in documents:
        doc_type = doc['type']
        number = doc['number']
        name = doc['name']
        print(f'{doc_type} "{number}" "{name}"')


def add():
    '''Добавить новый документ в каталог'''
    number = input('Введите номер документа: ')
    doc_type = input('Укажите тип документа: ')
    name = input('Укажите имя владельца: ')
    shelf_num = input('Укажите номер полки: ')
    if shelf_num not in directories.keys():
        print('Указанная полка не существует!')
        return
    
    documents.append({
        'type': doc_type,
        'number': number,
        'name': name
    })
    directories[shelf_num].append(number)
    print(f'Документ {number} успешно добавлен на полку №{shelf_num}')


def main():
    while True:
        command = input('Введите команду: ')
        if command == 'p':
            people()
        elif command == 's':
            shelf()
        elif command == 'l':
            doc_list()
        elif command == 'a':
            add()
        elif command == 'q':
            print('Выход')
            break
        else:
            print('Неизветсная команда')


if __name__ == '__main__':
    main()