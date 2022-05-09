file = open('C:/Users/Jupiter/Desktop/mygit/LearnInZeroBase/pythonTxt/aboutPython.txt','r',encoding='UTF8')
content = file.read().replace('Python','파이썬',1)
print(content)
file.close()

file = open('C:/Users/Jupiter/Desktop/mygit/LearnInZeroBase/pythonTxt/aboutPython.txt','w',encoding='UTF8')
file.write(content)
file.close()