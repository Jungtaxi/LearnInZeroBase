num1 = int(input('정수입력 : '))
num2 = int(input('정수입력 : '))

try :
    print(f'num1/num2 : {num1/num2}')
except Exception as e: 
    print('오류가 발생하였습니다.')
    print(f'exception : {e}')
print(f'num1+num2 = {num1+num2}')
print(f'num1-num2 = {num1-num2}')
