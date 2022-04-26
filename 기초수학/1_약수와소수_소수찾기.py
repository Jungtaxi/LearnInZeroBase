def is_decimal(num):
    if num <= 1:           # 0,1 관련 예외 처리
        return False
    for i in range(2,int(num**(1/2)+1)):
        if num%i==0:
            return False
    return True

for i in range(31):
    if is_decimal(i):
        print(i, end=' ')