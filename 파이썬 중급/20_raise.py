def div(n1,n2):
    if n2 != 0:
        print(f'n1/n2 = {n1/n2}')
    else :
        raise Exception('이처럼 에러날 때 내가 원하는 문구를 출력할 수 있습니다.')

n1 = int(input('input number1 : '))
n2 = int(input('input number2 : '))

try : 
    div(n1,n2)
except Exception as e :
    print(f'exception : {e}')