#초항과 공비가 주어졌을 때 n번째 항까지의 수열을 출력하는 프로그램을 만들어보자.
a1 = int(input('초항 입력 : '))
r = int(input('공비 입력 : '))
n = int(input('몇 번째 수열까지 구할까요? : '))
sum = a1*(1-r**n)//(1-r)

for i in range(1,n+1):
    print('{}번째 항은 : {}'.format(i,a1*(r**(i-1))))
print('등비 합은 : {}'.format(sum))


