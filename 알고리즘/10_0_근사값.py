import random
def apporxi(datas,input_num):
    nearnum = datas[0]
    for i in range(len(datas)):
        if abs(input_num-nearnum) > abs(input_num-datas[i]):
            nearnum = datas[i]
    return nearnum

numbers = random.sample(range(0,50),20)  # 중복 없이 20개의 수를 뽑는다.
print(numbers)
print(f'근사값은 {apporxi(numbers,30)}이다.')