students = {'s1':'홍길동', 's2':'스콘', 's3':'주노', 's4':'박승철', 's5':'차홍'}

# del students['s5']
# print(students)

# nonstudent = students.pop('s3')
# print(nonstudent)
# print(students)

# print(students.popitem())
# print(students)


# print(students.clear())
# print(students)

print(students.pop('s5',None))
print(students.pop('s6',None))
print(students)