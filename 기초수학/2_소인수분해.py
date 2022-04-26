#사용자가 입력한 수를 소인수 분해 하자
number = int(input())

n=2
while n<=number:
    if number % n == 0:
        number /= n
        print('소인수 : {}'.format(n))
    else:
        n+=1


#number에 x를 곱하면 y의 제곱이 된다고 한다.
number = int(input())
n=2
search_number = []
while n<=number:
    if number % n == 0:
        if search_number.count(n) == 0 :
            search_number.append(n)
        elif search_number.count(n) == 1 :
            search_number.remove(n)
        number/= n
    else:
        n+=1
print(search_number)