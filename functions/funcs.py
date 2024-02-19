def load_json_file():
    """Чтение файла json."""
    import json
    with open("C:/Users/User/PycharmProjects/kursovaya3/functions/operations.json", "r", encoding="utf8") as file:
        operations = file.read()
        operations_list = json.loads(operations)
    return operations_list


def sort_by_date():
    """Сортировка операций по дате."""
    operations_list = []
    for item in load_json_file():
        if item:
            operations_list.append(item)
    list_sorted_by_date = sorted(operations_list, key=lambda x: x['date'], reverse=True)
    return list_sorted_by_date


def last_executed_operation():
    """Вывод 5-ти последних EXECUTED операций."""
    sorted_list = []
    for item in sort_by_date():
        if item['state'] == 'EXECUTED':
            sorted_list.append(item)
    return sorted_list[0:5]


operations_list = load_json_file()
list_sorted_by_date = sort_by_date()
sorted_list = last_executed_operation()
