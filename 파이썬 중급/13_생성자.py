# class P_Class :
#     def __init__(self,pnum1,pnum2):
#         self.pnum1 = pnum1           # 매개 변수를 받아서 값을 초기화했다.
#         self.pnum2 = pnum2
#         print('P_Class의 __init__ 메소드가 호출되었습니다.')
# class C_Class(P_Class) :
#     def __init__(self,cnum1,cnum2):
#         P_Class.__init__(self,cnum1,cnum2)      #매개 변수를 빠트리지 않음에 유의한다.
#         self.cnum1 = cnum1
#         self.cnum2 = cnum2
#         print('C_Class의 __init__ 메소드가 호출되었습니다.')

# child = C_Class(10,11)



class P_Class :
    def __init__(self,pnum1,pnum2):
        self.pnum1 = pnum1           # 매개 변수를 받아서 값을 초기화했다.
        self.pnum2 = pnum2
        print('P_Class의 __init__ 메소드가 호출되었습니다.')
class C_Class(P_Class) :
    def __init__(self,cnum1,cnum2):
        super().__init__(cnum1,cnum2)      #self를 써주지 않아도 된다.
        self.cnum1 = cnum1
        self.cnum2 = cnum2
        print('C_Class의 __init__ 메소드가 호출되었습니다.')

child = C_Class(10,11)