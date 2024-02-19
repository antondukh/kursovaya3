from functions.funcs import last_executed_operation
from Clases.class_operation import Operation

# Список 5ти последних одобренных операций.
sort_list = last_executed_operation()
# Цикл для выводла операций в нужном формате
for i in sort_list:
    gg = Operation(i)
    print(gg.date())
    print(gg.from_to())
    print(f"""{gg.amount()}
    """)
