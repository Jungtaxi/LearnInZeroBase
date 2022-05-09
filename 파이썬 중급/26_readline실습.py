from url import *
scoreDic = {}
with open(url()+'과목별점수.txt','r') as f:
    line = f.readline()
    while line != '':
        temp = line.split()
        scoreDic[temp[0]] = temp[2]
        line = f.readline()
print(scoreDic)