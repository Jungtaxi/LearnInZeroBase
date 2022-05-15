def insert_sort(datas):
    for i in range(1,len(datas)):    # 0번째 요소는 뒤에 요소가 없으므로 1부터 시작합니다.
        for j in range(i,0,-1):      # 자기 자신과 이전 요소를 비교해가며, 이전 요소가 0이 될때 까지 비교합니다.
            if datas[j] < datas[j-1]:
                datas[j], datas[j-1] = datas[j-1],datas[j]
                print(datas)

datas = [0,5,11, 10, 2, 1, 0]
insert_sort(datas)