# 사용자한테 숫자를 입력받아 약수를 출력해보자.
number = int(input())
c = 0
for num in range(1,number+1):
    if number % num == 0:
        print('{}의 약수 : {}'.format(number,num))
        c+=1
print(f'약수는 총 {c}개')

