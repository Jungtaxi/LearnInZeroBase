def bubblesort(datas):
    for i in range(len(datas)):
        for j in range(len(datas)-i-1):
            if datas[j] > datas[j+1]:
                datas[j], datas[j+1] = datas[j+1], datas[j]
                print(datas)

datas = [10,2,7,21,3,0]
bubblesort(datas)
print(datas)
