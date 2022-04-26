# 두 수를 입력하여 최대 공약수와 공약수를 출력하자
num1, num2 = map(int, sorted(input().split()))
# num1, num2 = map(int, (input().split()).sort())   오류남
max_num = 1
for n in range(2,num1+1):
    if num1 % n == 0 and num2 % n == 0:
        max_num = n
print(max_num)

# 세 수 입력하여 최대 공약수를 출력하자
num1, num2, num3 = map(int, sorted(input().split()))
max_num = 1
for n in range(2,num1+1):
    if num1 % n == 0 and num2 % n == 0 and num3 % n == 0:
        max_num = n
print(max_num)