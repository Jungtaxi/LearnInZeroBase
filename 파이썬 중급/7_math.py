#수학 관련 내장함수
mylist = [2,5,3.14,58,10,2]
print(f'sum(mylist):{sum(mylist)}')                   #sum   합
print(f'max(mylist):{max(mylist)}')                   #max   최댓값
print(f'min(mylist):{min(mylist)}')                   #min   최솟값
print(f'pow(13,2):{pow(13,2)}')                       #pow   제곱
print(f'round(3.141592,3):{round(3.141592,3)}')       #round 반올림
print()

import math
print(f'math.fabs(-10):{math.fabs(-10)}')                #fabs 절대값
print(f'math.fabs(-10):{math.fabs(-0.1289)}')            #fabs 절대값
print(f'math.ceil(5.21):{math.ceil(5.21)}')              #ceil 올림
print(f'math.ceil(-4.31):{math.ceil(-4.31)}')            #ceil 올림
print(f'math.ceil(5.21):{math.ceil(5.21)}')              #ceil 올림
print(f'math.floor(-4.31):{math.floor(-4.31)}')          #floor 내림
print(f'math.floor(5.21):{math.floor(5.21)}')            #floor 내림
print(f'math.trunc(-4.31):{math.trunc(-4.31)}')          #trunc 버림
print(f'math.trunc(5.31):{math.trunc(5.31)}')            #trunc 버림
print(f'math.gcd(14,21):{math.gcd(1421)}')               #gcd 최대공약수
print(f'math.factorial(10):{math.factorial(10)}')        #factorial 팩토리얼
print(f'math.sqrt(10):{math.sqrt(10)}')                  #sqrt 제곱근
print()

import time
print(f'time.localtime():{time.localtime()}')          #현재 날짜, 월, 일, 시간
lt = time.localtime()

print(f'lt.tm_year:{lt.tm_year}')          #년도
print(f'lt.tm_mon:{lt.tm_mon}')            #월
print(f'lt.tm_mday:{lt.tm_mday}')          #일
print(f'lt.tm_hour:{lt.tm_hour}')          #시간
print(f'lt.tm_min:{lt.tm_min}')            #분
print(f'lt.tm_sec:{lt.tm_sec}')            #초
print(f'lt.tm_wday:{lt.tm_wday}')          #요일
print()

import random
print(f'random.random():{random.random()}')             #0 이상 1 미만의 실수
print(f'random.uniform(1,7):{random.uniform(1,7)}')      #1 이상 7 이하의 실수

print(f'random.randrange():{random.randrange(1,7)}')     #1 이상 7 미만의 정수
print(f'random.randrange():{random.randrange(7)}')       #0 이상 7 미만의 정수
print(f'random.randint():{random.randint(1,7)}')         #1 이상 7 이하의 정수)

abc = ['a','b','c','d']
random.shuffle(abc)
print(abc)                  #셔플

print(random.choice(abc))   #랜덤 선택
print(random.sample(abc,2))
print()

aaa = ['a','a','a']
print(random.choice(aaa))
print(random.sample(aaa,2))
