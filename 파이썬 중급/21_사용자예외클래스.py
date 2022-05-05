class NotUseZeroException(Exception):
    def __init__(self, n):
        super().__init__(f'{n}은 사용할 수 없습니다.')
def div(n1,n2):
    if n2 == 0 :
        raise NotUseZeroException(n2)
    print(f'n1/n2 = {n1/n2}')
num1 = int(input('숫자 1 : '))
num2 = int(input('숫자 2 : '))

try : 
    div(num1,num2)
except NotUseZeroException as z :
    print(f'Exception : {z}')