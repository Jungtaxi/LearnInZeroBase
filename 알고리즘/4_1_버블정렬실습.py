import random
import copy
def bubble(datas, deepCopy = True):          # 매개 변수를 하나 더 줬다.

    if deepCopy:
        copydatas = copy.copy(datas)         # 깊은 복사
    else : copydatas = datas                 # 얕은 복사

    for i in range(len(copydatas)):
        for j in range(len(copydatas)-i-1):
            if copydatas[j] > copydatas[j+1]:
                copydatas[j],copydatas[j+1] = copydatas[j+1],copydatas[j]
    
    return copydatas

students = [random.choice(range(170,185)) for _ in range(20)]
print(f'깊은 복사 ver. : \n{bubble(students,deepCopy=True)}')
print(f'원본 데이터 : \n{students}')
print()

print(f'얕은 복사 ver. : \n{bubble(students,deepCopy=False)}')
print(f'원본 데이터 : \n{students}')