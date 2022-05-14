import random

numbers = random.sample(range(50,101),20)
rank = [0 for _ in range(20)]

for idx,num1 in enumerate(numbers):
    for num2 in numbers:
        if num1 < num2 :
            rank[idx] += 1

print(f'numbers : {numbers}')
print(f'rank : {rank}')

for idx, num in  enumerate(numbers):
    print(f'num : {num}\t서열 {rank[idx]+1}위 입니다.')