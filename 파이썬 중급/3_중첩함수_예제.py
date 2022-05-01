def calculator(n1,n2,operator):
    def addCal():
        print(f'덧셈 : {round(n1+n2,2)}')
    def subCal():
        print(f'뺄셈 : {round(n1-n2,2)}')
    def mulCal():
        print(f'곱셈 : {round(n1*n2,2)}')
    def divCal():
        print(f'나눗셈 : {round(n1/n2,2)}')
    if operator == 1:
        addCal()
    elif operator == 2:
        subCal()
    elif operator == 3:
        mulCal()
    elif operator == 4:
        divCal()
    else:
        print('wrong key')

while True:
    n1 = float(input('첫번째 수 : '))
    n2 = float(input('두번째 수 : '))
    operator = float(input('1:덧셈,2:뺄셈,3:곱셈,4:나눗셈,5:종료'))
    if operator == 5 :
        print('bye~')
        break
    calculator(n1,n2,operator)
