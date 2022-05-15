import random
import copy
def select_sorted(datas, ASC = True):
    cdatas = copy.deepcopy(datas)
    if ASC:
        for i in range(len(cdatas)-1):
            min_idx = i
            for j in range(1+i,len(cdatas)):
                if cdatas[j]<cdatas[min_idx] :
                    min_idx = j
            cdatas[min_idx],cdatas[i] = cdatas[i],cdatas[min_idx]
    else :
        for i in range(len(cdatas)-1):
            max_idx = i
            for j in range(1+i,len(cdatas)):
                if cdatas[j]>cdatas[max_idx] :
                    max_idx = j
            cdatas[max_idx],cdatas[i] = cdatas[i],cdatas[max_idx]
    return cdatas


scorelist = [random.choice(range(0,101)) for _ in range(20)]
print(f'오름차순 : \n{select_sorted(scorelist,ASC=True)}')
print(f'내림차순 : \n{select_sorted(scorelist,ASC=False)}')
print(f'원본 데이터 : \n{scorelist}')