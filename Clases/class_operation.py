import string
import pprint
from functions.funcs import last_executed_operation

sort_list = last_executed_operation()
pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(sort_list[1])


class Operation:
    def __init__(self, date_, description_, from_, to_, amount_, code_):
        self.date_ = date_
        self.description_ = description_
        self.from_ = from_
        self.to_ = to_
        self.amount_ = amount_
        self.code_ = code_
        #print(self.date_, self.description_, self.from_, self.to_, self.amount_, self.code_)

    def date(self):
        s = f"{self.date_[8:10]}.{self.date_[5:7]}.{self.date_[0:4]}"
        return f"{s} {self.description_}"

    def from_to(self):
        s2 = ''.join(c for c in self.from_ if c in string.ascii_letters)
        numbers = ''.join(c if c.isdigit() else ' ' for c in self.from_).split()
        return f"{s2} {numbers[0][0:4]} {numbers[0][4:6]}** **** {numbers[0][-4::]} -> {self.to_[0:4]} **{self.to_[-4::]}"

    def amount(self):
        return f"{self.amount_} {self.code_}"


gg = Operation(sort_list[1]['date'], sort_list[1]['description'], sort_list[1]['from'], sort_list[1]['to'], sort_list[1]['operationAmount']['amount'], sort_list[1]['operationAmount']['currency']['name'])
#print(gg)
print(gg.date())
print(gg.from_to())
print(gg.amount())
