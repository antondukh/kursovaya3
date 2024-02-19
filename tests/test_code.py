from functions.funcs import *


def test_last_executed_operation():
    assert last_executed_operation() == sorted_list


def test_sort_by_date():
    assert sort_by_date() == list_sorted_by_date


def test_load_json_file():
    assert load_json_file() == operations_list
