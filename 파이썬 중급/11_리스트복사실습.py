playOriSco = [8.7,9.1,8.9,9.0,7.9,9.5,8.8,8.3]
playCopSco = playOriSco.copy()
playOriSco.sort()
playCopSco.sort()
playCopSco.pop()
playCopSco.pop(0)
avgOri = round(sum(playOriSco)/len(playOriSco),2)
avgCop = round(sum(playCopSco)/len(playCopSco),2)

print(f'원선수들 점수 {playOriSco}')
print(f'복사한 선수들 점수{playCopSco}')
print(f'원선수들 평균 {avgOri}')
print(f'복사한 선수들 평균 {avgCop}')
print(f'차이 : {round(avgOri - avgCop,2)}')

