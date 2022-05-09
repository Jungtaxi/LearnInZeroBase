from url import *

with open(url()+'hello.txt','r') as f :
    # print(f.readlines())
    # print(type(f.readlines()))
    line = f.readline()
    while line != '' :
        print(line, end='')
        line = f.readline()