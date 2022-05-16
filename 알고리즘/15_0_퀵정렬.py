import random
def quick_sort(datas):
    if len(datas) < 2 :
        return datas
    mid = len(datas) // 2
    small, same, big = [],[],[]
    for i in range(len(datas)):
        if datas[i] < datas[mid]:
            small.append(datas[i])
        elif datas[i] > datas[mid]:
            big.append(datas[i])
        else :
            same.append(datas[i])
    return quick_sort(small) + same + quick_sort(big)

datas = [random.choice(range(1,101)) for _ in range(20)]
print(quick_sort(datas))