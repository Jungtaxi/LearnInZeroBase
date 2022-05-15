import random
def mean(datas):
    total = 0
    for i in datas:
        total += i
    return total/len(datas)
nums = random.sample(range(0,101),10)
print(f'nums : {nums}')
print(f'mean : {mean(nums)}')