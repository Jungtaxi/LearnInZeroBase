class MaxAlgo:
    def __init__(self,datas):
        self.datas = datas
        self.max_value = 0
    def get_max_value(self):
        self.max_value = self.datas[0]
        for i in self.datas:
            if self.max_value < i :
                self.max_value = i
        return self.max_value

mylist = [11, 8, 76, 75, 10, 72, 68, 93, 35, 41, 64, 42, 30, 29, 65, 48, 56, 76, 29, 66]
maxalgo = MaxAlgo(mylist)
print(maxalgo.get_max_value())