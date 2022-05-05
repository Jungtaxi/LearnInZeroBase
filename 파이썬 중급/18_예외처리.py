n=6
while n > 0:
    try :
        int(input('input number : '))
    except :
        print(f'예외 처리 합니다. {n}개를 마저 입력해주세요.')
        continue
    n-=1