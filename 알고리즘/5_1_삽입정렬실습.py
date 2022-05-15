import random

def insert_sort(seq):
    for i in range(1,len(seq)):
        for j in range(i,0,-1):
            if seq[j] < seq[j-1]:
                seq[j],seq[j-1] = seq[j-1], seq[j]
            else : break

randomlist = [random.choice(range(1,1001)) for i in range(100)]
insert_sort(randomlist)
print(f'정렬된 난수들 : {randomlist}')
print(f'최댓값 : {randomlist[-1]}')
print(f'최솟값 : {randomlist[0]}')
