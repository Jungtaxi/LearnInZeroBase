# 반복문 사용
inputN = int(input('몇 팩토리얼까지 입력할까요!!! :\n'))
ans = 1
for i in range(1,inputN+1):
    ans *= i
print('{} 팩토리얼 : {}'.format(inputN,ans))

# 재귀함수 사용
def factorialFun(n):
    if n==1 : return 1
    return n*factorialFun(n-1)
print('{} 팩토리얼 : {}'.format(inputN,factorialFun(inputN)))

#math 모듈 사용
import math
print('{} 팩토리얼 : {}'.format(inputN,math.factorial(inputN)))
