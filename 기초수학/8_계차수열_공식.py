
a1 = int(input('수열의 초항 입력 : '))
n = int(input('몇번째 항까지 궁금하세요? : '))
b1 = int(input('계차수열의 초항 입력 : '))
d = int(input('계차수열의 공차 입력 : '))

b = b1 + d*(n-1)
a = a1 + (n-1)*(2*b1+d*(n-2))//2

print('{}번째 계수수열과 수열의 일반항은 {} 와 {} 입니다.'.format(n,b,a))