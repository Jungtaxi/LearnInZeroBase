scores = []
def addScore(s):
    scores.append(s)
    print('점수입력 완료')
def getScore():
    return scores
def totalScore():
    return sum(scores)
def avgScore():
    return round(totalScore()/len(scores),2)