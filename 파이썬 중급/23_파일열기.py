url = 'C:\\Users\\Jupiter\\Desktop\\mygit\\LearnInZeroBase\\pythonTxt\\'

# file = open(url + 'filemod.txt','w')
# file.write('\'w\'는 파일을 새로 만들거나 또는 글을 덮어 씌웁니다.')
# file.close()

# file = open(url + 'filemod.txt','a')
# file.write('\n\'a\'는 파일이 있다면 덧붙인다.')
# file.close()

# file = open(url + 'filemod2.txt','x')
# file.write('\n\'x\'는 파일이 없을 때만 적힙니다.')
# file.close()

file = open(url + 'filemod3.txt','r')
file.write('\'r\'은 파일이 없을 때는 에러가 납니다.')
file.close()

