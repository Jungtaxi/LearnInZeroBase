# mylist = ['홍길동','박찬호','이용규','강호동', '박승철','홍길동']
# print(mylist*3)

# print(mylist.index('스콘'))

# mylist2 = [1,2,3,4,5]
# element_wise = [x*y for x,y in zip(mylist2,mylist2)]
# print(element_wise)


mylist = ['홍길동','박승철','박찬호','이용규','강호동', '박승철','홍길동','박승철']

# idx = -1
# mylist.append('홍길동') # 보초법을 써서 홍길동을 찾아보자.
# while True :
#     idx = mylist.index('홍길동',idx+1,)
#     if idx == len(mylist)-1:
#         break
#     print(f'{idx} 에 위치합니다.')

print(mylist.count('홍길동'))