evenlist=[]
oddlist=[]
floatlist=[]

n=5
while n>0:
    try :
        inputNum = float(input('숫자 입력 : '))
    except :
        print('숫자만 입력하세요.')
    else :
        if inputNum % 1 != 0:
            floatlist.append(inputNum)
        elif inputNum % 2 != 0 :
            oddlist.append(int(inputNum))
        elif inputNum % 2 == 0 :
            evenlist.append(int(inputNum))
        n-=1
print(f'홀수 리스트 : {oddlist}')
print(f'짝수 리스트 : {evenlist}')
print(f'실수 리스트 : {floatlist}')
