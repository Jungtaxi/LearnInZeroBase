#주어진 첫항과 공차를 보고 등차 수열을 작성하여 보자.
a1 = int(input('첫 항 : '))
d = int(input('공차 : '))
n = int(input('몇항 까지 알고 싶은지 : '))

for i in range(n):
    print('{}번째 항 : {}'.format(i+1,d*i+a1))

print('등차수열의 합은 {}'.format((2*a1+(n-1)*d)*n//2))