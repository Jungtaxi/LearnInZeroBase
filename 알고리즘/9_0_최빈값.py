class MaxAlgo :
    def __init__(self,datas):
        self.datas = datas
        self.max_value = 0
        self.max_idx = 0
    def set_max_idx_value(self):
        self.max_value = self.datas[0]
        self.max_idx = 0
        for i in range(len(self.datas)):
            if self.datas[i] > self.max_value:
                self.max_value = self.datas[i]
                self.max_idx = i
    def get_max_idx(self):
        return self.max_idx
    def get_max_value(self):
        return self.max_value
        

datas = [1,3,7,6,7,7,7,12,12,17]
maxalgo1 = MaxAlgo(datas)
maxalgo1.set_max_idx_value()
print(f'max_value : {maxalgo1.get_max_value()}')
print(f'max_idx : {maxalgo1.get_max_idx()}')

indexes = [0 for _ in range(maxalgo1.get_max_value()+1)]
for i in datas:
    indexes[i] += 1
maxalgo2 = MaxAlgo(indexes)
maxalgo2.set_max_idx_value()
print(f'최빈값은 : {maxalgo2.get_max_idx()}')