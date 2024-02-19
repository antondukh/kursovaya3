from functions.funcs import last_executed_operation


def test_last_executed_operation():
    assert last_executed_operation() == ""
