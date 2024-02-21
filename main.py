from functions.funcs import *
from Clases.class_operation import Operation


# Список 5ти последних одобренных операций.

# Цикл для выводла операций в нужном формате
for i in right_date:
    gg = Operation(i)
    print(f"""{i['date']}, {i['description']}
{gg.from_to()}
{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}
    """)
