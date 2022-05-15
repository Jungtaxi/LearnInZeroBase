import random
scorelist = [random.choice(range(80,101)) for _ in range(100)]
print(scorelist)

index_list = [0 for _ in range(21)]
for i in scorelist:
    index_list[i-80] += 1
for idx,item in enumerate(index_list):

    print('{}점의 빈도 수 :\t{}\t{}'.format(idx+80,index_list[idx],'+'*(index_list[idx])))