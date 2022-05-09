# import time
# lt = time.localtime()
# dateStr = '[' + str(lt.tm_year) +'년 '+str(lt.tm_mon)+'월 '\
#     +str(lt.tm_mday)+'일] '
# todaySchedule = input('오늘 일정 : ')
# file = open('C:\\Users\\Jupiter\\Desktop\\mygit\\LearnInZeroBase\\pythonTxt\\practice01.txt','w')
# file.write(dateStr+todaySchedule)
# file.close()

import time
dateStr = '[' + time.strftime('%Y-%m-%d %I:%M:%S %p') + ']'
todaySchedule = input('집안 일정 :')

file=open('C:\\Users\\Jupiter\\Desktop\\mygit\\LearnInZeroBase\\pythonTxt\\practice02.txt', 'w')
file.write(dateStr + todaySchedule)
file.close()
file=open('C:\\Users\\Jupiter\\Desktop\\mygit\\LearnInZeroBase\\pythonTxt\\practice02.txt', 'r')
print(file.read())
file.close()