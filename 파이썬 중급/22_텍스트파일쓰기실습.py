import time
lt = time.localtime()
dateStr = '[' + str(lt.tm_year) +'년 '+str(lt.tm_mon)+'월 '\
    +str(lt.tm_mday)+'일] '
todaySchedule = input('오늘 일정 : ')
file = open('C:\\Users\\Jupiter\\Desktop\\mygit\\LearnInZeroBase\\pythonTxt\\practice01.txt','w')
file.write(dateStr+todaySchedule)
file.close()