datas = [3,2,5,7,9,1,0,8,6,4]
print(f'datas:{datas}')
print(f'len : {len(datas)}')

searchData = int(input('찾으려는 숫자 입력 : '))
searchResultIdx = -1

n=0
while True:
    if datas[n] == searchData:
        searchResultIdx = n
        break
    n += 1
    if n == len(datas):
        break
print(f'찾는 값의 인덱스는 {searchResultIdx} 입니다.')