class MaxAlgo :
    def __init__(self, datas):
        self.datas = datas
        self.max_chr = 0
    def get_max_char(self):
        self.max_chr = self.datas[0]
        for i in self.datas:
            if ord(self.max_chr) < ord(i):
                self.max_chr = i
        return self.max_chr

datas = ['c','A','Q','q','e','F','p']
algo = MaxAlgo(datas)
print(algo.get_max_char())