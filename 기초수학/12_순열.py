def permu_(numL, numR) :
    result = 1
    for i in range(numL,numL-numR,-1):
        result *= i
        print(i)
    return result

numL = int(input('몇 개 중에서 :'))
numR = int(input('몇 개를 순서를 고려해 뽑을건가요\n : '))
print(permu_(numL,numR))


# 원순열
# 4명의 친구가 원탁 테이블에 앉을 수 있는 순서의 경우의 수를 계산해보자.
n = 4
ans = 1
for i in range(1,n):
    ans *= i
print(ans)