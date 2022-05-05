try :
    inputData = input('정수를 입력해주세요 : ')
    inputNum = int(inputData)
except :
    print('정수가 아닙니다!!')
    print('정수가 더 멋있어요!')
else :
    print('이것은 정수가 맞군요.')
    print('정수 좋아')
finally :
    print(f'당신은 {inputData}를 입력하셨습니다.')