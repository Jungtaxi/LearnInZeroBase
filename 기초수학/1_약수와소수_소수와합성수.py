numbers = int(input())
for number in range(2,numbers+1):
    flag=True
    for i in range(2,int((number)**(1/2)+1)):
        if number % i == 0:
            flag = False
            break
    if flag :
        print('{}는 소수'.format(number))
    else :
        print('{}는 \t\t 합성수'.format(number))
