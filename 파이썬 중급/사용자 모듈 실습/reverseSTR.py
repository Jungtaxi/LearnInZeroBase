# 방법 1
def reverse1(word) :
    return word[::-1]
# 방법 2
def reverse2(word) :
    return ''.join(reversed(word))
# 방법 3
def reverse3(word) :
    result = list(word)
    result.reverse()
    return ''.join(result)