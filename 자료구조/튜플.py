student1 = ('홍길동','김철수','스콘')
student2 = ('김영희','김말숙','옥주현')
student3 = student1 + student2

print(student3)

number1 = (1,2,3,4,5)
number2 = (3,4,5,6,7)
for num in number2:
    if num not in number1:
        number1 = number1 + (num, )
print(number1)