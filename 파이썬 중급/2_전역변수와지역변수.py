# 전역변수
# number = 10

# def print_number():
#     print(f'number:{number}')

# print_number()

# 지역변수
# number2 = 20             # 얘는 전역변수

# def print_number2():
#     number2 = 100        # 얘는 지역변수
#     print(f'number2:{number2}')
# print_number2()
# print(f'number2:{number2}')

# # 지역변수
# def print_number3():
#     number3 = 150
#     print(f'number3:{number3}')
# print_number3()
# print(number3)

#global 키워드
number4 = 20             # 얘는 전역변수

def print_number2():
    global number4
    number4 = 100        # 얘는 위에서 선언한 전역변수와 동일한 애
    print(f'number2:{number4}')
print_number2()
print(f'number2:{number4}')