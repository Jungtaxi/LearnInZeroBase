
a1 = int(input('수열의 초항 입력 : '))
n = int(input('몇번째 항까지 궁금하세요? : '))
b1 = int(input('계차수열의 초항 입력 : '))
d = int(input('계차수열의 공차 입력 : '))

k = 1
while k <= n :
    if k == 1 :
        a = a1
        b = b1
        print('a의 {}번째 값은 {}'.format(k,a))
        print('b의 {}번째 값은 {}'.format(k,b))
        print('------------------------------')
        k += 1
        continue
    a += b
    b += d
    print('a의 {}번째 값은 {}'.format(k,a))
    print('b의 {}번째 값은 {}'.format(k,b))
    print('------------------------------')
    
    k += 1