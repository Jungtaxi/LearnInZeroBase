from url import *

file = open(url()+'oddNum.txt','a')
userNum = int(input('숫자를 입력하세요 : '))
for i in range(2,userNum+1):
    if i == 2 :
        file.write(f'\n{i}')
        continue
    for j in range(2,i) :
        if i%j==0:
            break
    else:
        file.write(f', {i}')
file.close()