scores = [9,8,5,7,6,10]

# 얕은 복사
scoresCopy = scores
print(f'id(scores):{id(scores)}')     #id는 메모리에 할당된 값을 찍어보는 것
print(f'id(scoresCopy):{id(scoresCopy)}')
print()

#깊은 복사1
scoresCopy1 = []
for s in scores:
    scoresCopy1.append(s)
print(f'id(scores) : {id(scores)}')
print(f'id(scoresCopy1) : {id(scoresCopy1)}')
print()

# 깊은 복사2
scoresCopy2 = []
scoresCopy2.extend(scores)
print(f'id(scores) : {id(scores)}')
print(f'id(scoresCopy2) : {id(scoresCopy2)}')
print()

# 깊은 복사3
scoresCopy3 = scores.copy()
print(f'id(scores) : {id(scores)}')
print(f'id(scoresCopy3) : {id(scoresCopy3)}')
print()

# 깊은 복사4
scoresCopy4 = scores[:]
print(f'id(scores) : {id(scores)}')
print(f'id(scoresCopy4) : {id(scoresCopy4)}')
print()