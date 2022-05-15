def select_sort(datas):
    for i in range(len(datas)-1):
        min_index = i
        for j in range(1+i,len(datas)):
            if datas[j] < datas[min_index]:
                min_index = j
        datas[i],datas[min_index] = datas[min_index],datas[i]

datas = [4,2,5,1,3]
select_sort(datas)
print(datas)