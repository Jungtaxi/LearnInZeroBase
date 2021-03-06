# 1부터 30까지 숫자 중 5로 나눈 몫과 나머지가 모두 소수인 숫자들
def is_decimal(num):
    if num <= 1:
        return False
    for i in range(2,int(num**(1/2))+1):
        if num%i==0:
            return False
    return True

for num in range(1,31):
    if is_decimal(num%5) and is_decimal(num//5):
        print(num, end = ' ')