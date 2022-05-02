import random
rNum = random.randint(1,10)
print(f'rNum:{rNum}')

# rNums = random.sample(range(1,101),10)
# print(f'rNums:{rNums}')

rNums = random.sample((1,2,3,4,5,6,3.3,7,8,20,101),10)
print(f'rNums:{rNums}')

