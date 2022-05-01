# [실습1] 사용자가 가로 세로 길이를 입력하면 삼각형과 사각형 넓이를 출력해주자.
def print_area():
    print('사각형 넓이는 {}'.format(width*height))
    print('삼각형 넓이는 {}'.format(width*height//2)) 
width = int(input('가로 길이 : '))
height = int(input('세로길이 : '))
print_area()

# [실습2] 사용자가 가로 세로 길이를 입력하면 삼각형과 사각형 넓이를 출력해주자.
total_visit = 0

def count_total_visit():
    global total_visit
    total_visit += 1
    print(f'방문객 수는 {total_visit}명 입니다.')

count_total_visit()
count_total_visit()
count_total_visit()