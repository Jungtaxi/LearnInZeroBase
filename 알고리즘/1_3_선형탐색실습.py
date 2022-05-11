numbers = [4,7,10,2,4,7,0,2,7,3,9]
searchNum = int(input())
resultIdx = []
idx = 0
numbers.append(searchNum)
while True :
    if numbers[idx] == searchNum:
        if idx != len(numbers)-1:
            resultIdx.append(idx)
        else : break
    idx +=1
print(f'{resultIdx}에 위치해 있습니다.\
그리고 {len(resultIdx)}개의 {searchNum}이 존재합니다.')
