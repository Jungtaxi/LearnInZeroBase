from url import *

# file = open(url()+'practice03.txt','w')
# file.write('let\' practice with ~ as ~')
# file.close()

with open(url()+'practice03.txt','a') as f:
    f.write('\n this is the with ~ as 구문')

with open(url()+'practice03.txt','r') as f :
    print(f.read())