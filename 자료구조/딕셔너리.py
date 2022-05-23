# students = {'s1':'홍길동', 's2':'스콘', 's3':'주노', 's4':'박승철', 's5':'차홍'}

# s1info = {'이름' : '홍길동',
#         '나이' : 28, 
#         '키' : 180, 
#         '취미' : ['농구','축구']}


# print(s1info['이름'])
# print(s1info['나이'])
# print(s1info['키'])
# print(s1info['취미'])
# print(s1info['좋아하는 노래'])

# print(s1info.get('이름'))
# print(s1info.get('나이'))
# print(s1info.get('키'))
# print(s1info.get('취미'))
# print(s1info.get('좋아하는 노래'))

myinfo = {}
myinfo['이름'] = '스콘'
myinfo['메일'] = 'callmescone'
myinfo['전공'] = '국제통상'
myinfo['전공'] = '컴퓨터'
print(myinfo)
print(len(myinfo))

ks = myinfo.keys()
print(ks)
print(type(ks))
print()

vs = myinfo.values()
print(vs)
print(type(vs))
print()

items = myinfo.items()
print(items)
print(type(items))

for i in myinfo.keys():
    print(f'{i} : {myinfo[i]}')
print()

for i in myinfo:
    print(f'{i} : {myinfo[i]}')