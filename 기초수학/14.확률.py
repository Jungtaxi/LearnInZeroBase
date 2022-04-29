def combina_():
    numL = int(input('numL 입력 : '))
    numR = int(input('numR 입력 : '))
    result = 1
    for i in range(numL,numL-numR,-1):
        result *= i
    for i in range(1,numR+1):
        result /= i
    return result

sample = combina_()
event1 = combina_()
event2 = combina_()

print('probability : {}%'.format(round((event1*event2/sample)*100, 2)))