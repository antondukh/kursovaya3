class Operation:
    def __init__(self, operation):
        self.operation = operation

    def from_to(self):
        """Вывод откуда -> куда."""
        if 'from' in self.operation:
            s2 = ''.join([x for x in self.operation['from'] if not x.isdigit()])
            numbers = ''.join(c if c.isdigit() else ' ' for c in self.operation['from']).split()
            from_ = f"{s2} {numbers[0][0:4]} {numbers[0][4:6]}** **** {numbers[0][-4::]}"
            to_ = f"-> {self.operation['to'][0:4]} **{self.operation['to'][-4::]}"
            return f"{from_} {to_}"
        else:
            to_ = f"{self.operation['to'][0:4]} **{self.operation['to'][-4::]}"
            return to_
