from url import *
import random

# with open(url()+'writlines실습.txt','a') as f:
#     randN = random.sample(range(1,46),7)
#     f.write('\n')
#     for i in randN:
#         f.write(f'{i} ')

with open(url()+'writlines실습.txt','w') as f:
    randN = random.sample(range(1,46),7)
    f.writelines(str(item)+'\n' for item in randN)

with open(url()+'writlines실습.txt','r') as f:
    print(f.read())