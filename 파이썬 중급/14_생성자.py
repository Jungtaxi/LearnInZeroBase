class Midterm :
    def __init__(self,s1,s2,s3):
        print('Midterm __init__()')
        self.mid_kor = s1
        self.mid_eng = s2
        self.mid_math = s3
    def print_score(self):
        print(f'중간 국어점수 : {self.mid_kor}')
        print(f'중간 영어점수 : {self.mid_eng}')
        print(f'중간 수학점수 : {self.mid_math}')
class EndExam(Midterm):
    def __init__(self,s1,s2,s3,s4,s5,s6):
        print('EndExam __init__()')
        super().__init__(s1,s2,s3)
        self.end_kor = s4
        self.end_eng = s5
        self.end_math = s6
    def print_score(self):
        super().print_score()
        print(f'기말 국어점수 : {self.end_kor}')
        print(f'기말 영어점수 : {self.end_eng}')
        print(f'기말 수학점수 : {self.end_math}')
    def get_total_score(self):
        total = self.mid_kor+self.mid_eng+self.mid_math
        total += self.end_kor+self.end_eng+self.end_math
        return total
    def get_avg_score(self):
        return self.get_total_score() / 6

end_exam = EndExam(85,90,75,83,90,95)
end_exam.print_score()
print(f'전체 총점 : {end_exam.get_total_score()}')
print(f'전체 평점 : {end_exam.get_avg_score()}' )