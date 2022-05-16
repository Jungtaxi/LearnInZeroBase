def moveDisc(cnt, from_bar, to_bar, via_bar):
    global anslist
    if cnt == 1:
        anslist.append([from_bar,to_bar])
    else:
        moveDisc(cnt-1,from_bar,via_bar,to_bar)
        moveDisc(1,from_bar,to_bar,via_bar)
        moveDisc(cnt-1,via_bar,to_bar,from_bar)

cnt = int(input())
anslist = []
moveDisc(cnt,1,3,2)
print(len(anslist))
for li in anslist:
    print(f'{li[0]} {li[1]}')