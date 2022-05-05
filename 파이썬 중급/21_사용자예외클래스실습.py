class PasswordLengthShortException(Exception) :
    def __init__(self,password):
        super().__init__(f'{password}는 길이가 5 미만 입니다.')
class PasswordLengthLongException(Exception) :
    def __init__(self,password):
        super().__init__(f'{password}는 길이가 10 초과 입니다.')
class PasswordWrongException(Exception) :
    def __init__(self,password):
        super().__init__(f'{password}는 잘못된 패스워드 입니다.')
def check_password(password):
    if len(password)<5:
        raise PasswordLengthShortException(password)
    elif len(password)>10:
        raise PasswordLengthLongException(password)
    elif password.isalpha() or password.isdigit():
        raise PasswordWrongException(password)
    return True

while True:
    password = input('input admin password : ')
    try :
        check_password(password)
    except Exception as e :
        print(f'Exception : {e}')
    else :
        print('패스워드가 입력되었습니다.') 
        break