inputN = int(input('n 항 입력 : '))
n = 1
c = 0
searchN = 0
flag = True
while flag:
    for i in range(1,n+1):
        print(i, end=' ')
        c += 1
        if c == inputN:
            searchN = i
            flag = False
            break
    n +=1
    print()
print('{}항 값은 {}'.format(inputN,searchN))