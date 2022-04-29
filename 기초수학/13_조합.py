def combina_(numL,numR):
    result=1
    for i in range(numL,numL-numR,-1):
        result *= i
    for i in range(1,numR+1):
        result //= i
    return result

numL = int(input('몇 개 중에서 : '))
numR = int(input('몇 개 선택 : '))
print(combina_(numL,numR))
