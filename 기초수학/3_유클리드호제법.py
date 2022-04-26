# 유클리드 호제법으로 최대공약수와 공약수 구하기
num1, num2 = map(int, input().split())
temp1, temp2 = num1,num2
while temp2>0 :
    temp = temp2
    temp2 = temp1 % temp2
    temp1 = temp
print('{}과 {}의 최대 공약수는 {}'.format(num1,num2,temp1))

for i in range(1,temp1+1):
    if temp1 % i == 0:
        print('{}과 {}의 공약수는 {}'.format(num1,num2,i))