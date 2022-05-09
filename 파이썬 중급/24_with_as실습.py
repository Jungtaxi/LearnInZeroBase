from url import *
import random

def lotto(randN):
    with open(url()+'로또추천.txt','a') as f:
        for idx, i in enumerate(randN):
            if idx == 0 :
                f.write(f'{i}')
            elif idx == len(randN)-1:
                f.write(f'\nBonus : {i}\n')
            else :
                f.write(f', {i}')
randomNumbers = random.sample(range(1,46),7)
print(randomNumbers)
lotto(randomNumbers)