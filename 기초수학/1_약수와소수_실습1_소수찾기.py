def is_decimal(num):
    if num <= 1:           # 0,1 관련 예외 처리
        return False
    if num == 2:           # 2 관련 예외 처리
        return True
    for i in range(2,num//2+2):
        if num%i==0:
            return False
    return True

for i in range(31):
    if is_decimal(i):
        print(i, end=' ')