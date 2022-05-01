triangleArea = lambda width, height : round(width*height/2,2)
squareArea = lambda width,height : round(width*height,2)
circleArea = lambda r : round(r*r*3.14,2)

width = int(input('가로 길이 : '))
height = int(input('높이 : '))
r = int(input('반지름 : '))

print('삼각형 넓이는 : {}'.format(triangleArea(width,height)))
print('사각형 넓이는 : {}'.format(squareArea(width,height)))
print('원 넓이는 : {}'.format(circleArea(r)))
