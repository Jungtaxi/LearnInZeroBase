class Calculator :
    def __init__(self):
        self.number1 = 0
        self.number2 = 0
        self.result = 0
    def add(self):
        self.result = self.number1 + self.number2
        return self.result
cal = Calculator()
cal.number1 = int(input('넘버원 : '))
cal.number2 = int(input('넘버투 : '))
print(f'cal.add():{cal.add()}')