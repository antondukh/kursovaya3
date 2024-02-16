def load_json_file():
    """Чтение файла json и вывод переменной."""
    import json
    with open("operations.json", "r", encoding="utf8") as file:
        operations = file.read()
        operations_list = json.loads(operations)
    return operations_list


def sort_by_date():
    """Сортировка операций по дате и вывод 5-ти последних операций."""
    sorted_operation_list = []
    for person in load_json_file():
        if person:
            sorted_operation_list.append(person)

    sorted_list = sorted(sorted_operation_list, key=lambda x: x['date'], reverse=True)
    return sorted_list[0:5]


print(sort_by_date())

