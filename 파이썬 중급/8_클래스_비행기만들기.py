class Airplane :
    def __init__(self,color,length,weight):
        self.color = color
        self.length = length
        self.weight = weight
    def get_info(self):
        print(f'self.color : {self.color}')
        print(f'self.length : {self.length}')
        print(f'self.weight : {self.weight}')
    def do_depart(self):
        print('depaaaart!!!!!')
    def do_arrive(self):
        print('aaaaaarive!!!!!')

airplane1 = Airplane('red',500,1000)
airplane1.get_info()
airplane1.do_depart()
airplane1.do_arrive()