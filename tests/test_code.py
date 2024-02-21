from functions.funcs import *
from Clases.class_operation import *


test_executed = [
    {'state': 'EXECUTED'},
    {'state': 'CANCELLED'},
    {'state': 'EXECUTED'},
    {'state': 'CANCELLED'},
    {'state': 'EXECUTED'},
    {'state': 'EXECUTED'},
    {'state': 'EXECUTED'},
    {'state': 'CANCELLED'},
    {'state': 'EXECUTED'},]


def test_last_executed_operation():
    assert last_executed_operation(test_executed) == [
        {'state': 'EXECUTED'},
        {'state': 'EXECUTED'},
        {'state': 'EXECUTED'},
        {'state': 'EXECUTED'},
        {'state': 'EXECUTED'},]


test_date = [
    {'date': '12'},
    {'date': '14'},
    {'date': '1'},
    {'date': '17'},]


def test_sort_by_date():
    assert sort_by_date(test_date) == [
        {'date': '17'},
        {'date': '14'},
        {'date': '12'},
        {'date': '1'},]


test_right_date = [
    {'date': '2019-12-08T22:46:21.935582'},
    {'date': '2019-12-07T06:17:14.634890'}
    ]


def test_date_r():
    assert date_r(test_right_date) == [
        {'date': '08.12.2019'},
        {'date': '07.12.2019'}
        ]


from_ = {'from': 'Visa Classic 2842878893689012',
         'to': 'Счет 35158586384610753655'}
to_ = {'to': 'Счет 90424923579946435907'}


def test_class():
    assert Operation(to_).from_to() == 'Счет **5907'
    assert Operation(from_).from_to() == "Visa Classic  2842 87** **** 9012 -> Счет **3655"
