class Car :
    def __init__(self,col,len):      # self는 차
        self.color = col             # 차의 색깔 (속성)
        self.length = len            # 차의 길이 (속성)

    def do_stop(self):               # 정지하는 기능
        print('stop!!!!')
    def do_start(self):              # 전진하는 기능
        print('start!!!')
    def print_car_info(self):        # 자동차 속성 프린트
        print(self)
        print(f'self.color : {self.color}')
        print(f'self.length : {self.length}')

car1 = Car('red',200)
car2 = Car('blue',300)

car1.print_car_info()
car2.print_car_info()

car1.do_start()
car2.do_start()