input_n = int(input('n 입력 : '))

value = 0
value_pre1 = 0
value_pre2 = 0
sum = 0
n=1
while n <= input_n:
    if n==1 or n==2:
        value = 1
        sum +=value
        value_pre1 = value
        n+=1
        continue
    value_pre2 = value_pre1
    value_pre1 = value
    value = value_pre1 + value_pre2
    sum += value
    n+=1
print('{}번째 항은 {}'.format(input_n, value))
print('{}번째까지의 합은 {}'.format(input_n, sum))
