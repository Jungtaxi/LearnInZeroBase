inputN = int(input())
flag = True
n=1
c=0
ans=0
while flag :
    for i in range(1,n+1):
        print('{}/{}'.format(i,n+1-i),end=' ')
        c += 1
        if c == inputN :
            ans = '{}/{}'.format(i,n+1-i)
            flag = False
            break
    n += 1
    print()
print('{}항은 {}'.format(inputN,ans))