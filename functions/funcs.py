import json

with open("C:/Users/User/PycharmProjects/kursovaya3/operations.json", 'r', encoding="utf8") as file:
    operations = file.read()
    json_file = json.loads(operations)


def sort_by_date(json_file):
    """Сортировка операций по дате."""
    operations_list = []
    for item in json_file:
        if item:
            operations_list.append(item)
    list_sorted_by_date = sorted(operations_list, key=lambda x: x['date'], reverse=True)
    return list_sorted_by_date


list_date = sort_by_date(json_file)


def last_executed_operation(list_date):
    """Вывод 5-ти последних EXECUTED операций."""
    sorted_lst = []
    for item in list_date:
        if item['state'] == 'EXECUTED':
            sorted_lst.append(item)
            if len(sorted_lst) == 5:
                break
    return sorted_lst


last_executed_operations = last_executed_operation(list_date)


def date_r(last_executed_operations):
    """Изменение даты в формат dd.mm.yyyy."""
    for i in last_executed_operations:
        i['date'] = f"{i['date'][8:10]}.{i['date'][5:7]}.{i['date'][0:4]}"
    return last_executed_operations


right_date = date_r(last_executed_operations)
