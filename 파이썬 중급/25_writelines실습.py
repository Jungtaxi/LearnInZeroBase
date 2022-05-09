from url import *

scoreDic = {'kor':85, 'eng':90, 'mat':92, 'sci':79, 'his':82}

with open(url()+'과목별점수.txt','w') as f :
    f.writelines(key+'\t: '+ str(scoreDic[key])+'\n' for key in scoreDic.keys())

# with open(url()+'과목별점수.txt','w') as f :
#     print(scoreDic, file=f)