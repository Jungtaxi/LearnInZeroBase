def binary_search(array,target,start,end):
    while start<= end:
        mid = (start + end)//2
        if array[mid] == target :
            print(f'mid : {array[mid]}')
            return mid
        elif array[mid] < target :
            start = mid+1
            print(f'mid : {array[mid]}')
        else :
            end = mid - 1
            print(f'mid : {array[mid]}')
    return None

array = [1,2,3,4,5,6,7,8,9,10,11]
print(f'array : {array}')
target = int(input('찾을 데이터는 : '))
print(f'데이터는 {binary_search(array,target,0,len(array))}번 인덱스에 있습니다.')
