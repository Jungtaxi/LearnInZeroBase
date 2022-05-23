secret = '27156231'
decode = list(secret)
decode.reverse()
decode = list(map(int,decode))

i = 0
while i < len(decode):
    decode.insert(i+2,decode[i]*decode[i+1])
    i += 3

print(''.join(map(str,decode)))
