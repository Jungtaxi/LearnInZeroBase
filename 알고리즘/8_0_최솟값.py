class MinAlgo:
    def __init__(self,datas):
        self.datas = datas
        self.min_value = 0
    def get_min_value(self):
        self.min_value = self.datas[0]
        for i in self.datas:
            if self.min_value > i :
                self.min_value = i
        return self.min_value

mylist = [5, 2, 4, 1, 3]
algo = MinAlgo(mylist)
print(algo.get_min_value())