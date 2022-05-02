# import lottomachine

# lottoNumbers = lottomachine.getLottoNum()
# print(f'lottoNumbers : {lottoNumbers}')


# import reverseSTR
# word = 'Hello world!'
# print('첫번째 방법 : '+reverseSTR.reverse1(word))
# print('두번째 방법 : '+reverseSTR.reverse2(word))
# print('세번째 방법 : '+reverseSTR.reverse3(word))


# from calculator import add as a
# print( a(1,2))

# from calculator import *
# print(add(1,1))
# print(sub(1,1))

from score import *

korScore = int(input('국어 점수 : '))
mathScore = int(input('수학 점수 : '))
engScore = int(input('영어 점수 : '))
addScore(korScore)
addScore(mathScore)
addScore(engScore)
print(f'점수 : {getScore()}')
print(f'총점 : {totalScore()}')
print(f'평점 : {avgScore()}')
