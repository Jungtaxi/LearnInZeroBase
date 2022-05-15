# 유클리드 호제
def gcd(a,b):
    c = a % b
    if c == 0 :
        return b
    return gcd(b,c)


a, b = map(int,input('최대 공약수를 구하고픈 두 수 ? : ').split())
print(f'{a}, {b}의 최대공약수는 {gcd(a,b)}')