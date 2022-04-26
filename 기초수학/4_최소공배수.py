# 두 개의 수를 입력하면 최소 공배수를 출력하는 코드를 작성하자.
num1, num2 = map(int, sorted(input().split()))
maxNum = 1
for n in range(2,num1+1):
    if num1%n == 0 and num2%n == 0 :
        maxNum=n
print('{}와 {}의 최대공약수는 {}입니다.'.format(num1,num2,maxNum))

minNum = num1*num2 // maxNum
print('{}와 {}의 최소공배수는 {}입니다.'.format(num1,num2,minNum))

# 세 개의 수를 가지고 해보자.
num1, num2, num3 = map(int, sorted(input().split()))
maxNum = 1
for n in range(2,num1+1):
    if num1%n==0 and num2%n==0 and num3%n==0 :
        maxNum=n
print('{}, {}, {} 최대공약수는 {}입니다.'.format(num1,num2,num3,maxNum))

minNum = num1*num2*num3 // (maxNum**2)
print('{}, {}, {} 최소공배수는 {}입니다.'.format(num1,num2,num3,minNum))
