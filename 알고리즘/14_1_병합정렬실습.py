import random
import copy
def merge_sort(datas):
    if len(datas) == 1:
        return datas
    mid = len(datas)//2
    left = merge_sort(datas[:mid])
    right = merge_sort(datas[mid:])
    merge_list = []
    i,j = 0,0
    while True:
        if i == len(left):
            merge_list += right[j:]
            break
        elif j == len(right):
            merge_list += left[i:]
            break
        elif left[i] < right[j]:
            merge_list.append(left[i])
            i += 1
        else : 
            merge_list.append(right[j])
            j += 1
    return merge_list


original = [random.choice(range(1,101)) for _ in range(10)]


copyver = copy.deepcopy(original)
print('오름차순 정렬 :')
print(merge_sort(copyver))

print('내림차순 정렬 :')
copyver2 = copy.deepcopy(original)
copyver2 = [ -i for i in copyver2 ]
print([ -i for i in merge_sort(copyver2)])

print('원본 데이터 : ')
print(original)