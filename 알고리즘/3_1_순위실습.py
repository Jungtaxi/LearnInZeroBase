import random

class RankDevi:
    def __init__(self, mid_score, final_score):
        self.mid_score = mid_score
        self.final_score = final_score
        self.mid_rank = [0 for _ in range(20)]
        self.final_rank = [0 for _ in range(20)]
        self.rank_deviation = [0 for _ in range(20)]
    
    def set_rank(self, scorelist, rank):
        for idx,num1 in enumerate(scorelist):
            for num2 in scorelist:
                if num1 > num2:
                    rank[idx] += 1 
    
    def set_mid_rank(self):
        self.set_rank(self.mid_score,self.mid_rank)

    def set_final_rank(self):
        self.set_rank(self.final_score,self.final_rank)

    
    def Rank_deviation(self):
        for i in range(20):
            if self.mid_rank[i] > self.final_rank[i] :
                self.rank_deviation[i] = '↑'+str(self.mid_rank[i]-self.final_rank[i])
            elif self.mid_rank[i] < self.final_rank[i] :
                self.rank_deviation[i] = '↓'+str(self.final_rank[i]-self.mid_rank[i])
            else:
                self.rank_deviation[i] = '='

mid_score = random.sample(range(1,101),20)
final_score = random.sample(range(1,101),20)

rank_list = RankDevi(mid_score,final_score)
rank_list.set_mid_rank()
print(f'mid_score : {mid_score}\n rank : {rank_list.mid_rank}')
rank_list.set_final_rank()
print(f'final_score : {final_score}\n rank : {rank_list.final_rank}')
rank_list.Rank_deviation()

for i in range(20):
    print(f'mid_rank:{rank_list.mid_rank[i]}\tfinal_rank:{rank_list.final_rank[i]}\tDeviation:{rank_list.rank_deviation[i]}')
