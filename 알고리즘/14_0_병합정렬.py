def merge_sort(datas):
    if len(datas) == 1:
        return datas
    mid = len(datas)//2
    left = merge_sort(datas[:mid])
    right = merge_sort(datas[mid:])
    mergelist = []
    i, j = 0, 0
    while True:
        if i == len(left):
            mergelist += right[j:]
            break
        elif j == len(right):
            mergelist += left[i:]
            break
        elif left[i] < right[j]:
            mergelist.append(left[i])
            i += 1
        else :
            mergelist.append(right[j])
            j += 1
    return mergelist

datas = [8,1,4,3,2,5,10,6]
print(merge_sort(datas))