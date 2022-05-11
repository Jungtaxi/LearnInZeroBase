me = [1,3,5,6,7]
friend = [2,3,5,8,10]

addlist = me+friend
result = []
for idx,number in enumerate(addlist):
    if addlist[idx+1:].count(number)>0:
        continue
    result.append(number)
print(result)

# print('aaabcaa'.count('a', 3))
# print(['a','b','a'].count('a', 1))
