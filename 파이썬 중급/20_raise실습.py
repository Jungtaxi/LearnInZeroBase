# 10글자 초과하면 MMS로 전환, 10글자 이내면 SMS로 전환하는 프로그램을 만들어보자.

def MMS(msg):
    if len(msg) <= 10 :
        raise Exception('10글자 이하 입니다. SMS로 전환해주세요.',1)
    else:
        print('msg 발송!')
def SMS(msg):
    if len(msg) >= 10 :
        raise Exception('10글자 이상 입니다. MMS로 전환해주세요.',2)
    else:
        print('MMS 발송!')

msg = input('보낼 메세지 : ')
try : 
    MMS(msg)
except Exception as e :
    print(f'Exception :{e.args[1]}번 에러입니다. {e.args[0]}')
    if e.args[1] == 1 :
        SMS(msg)
    elif e.args[1] == 2 :
        MMS(msg)