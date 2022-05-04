class Robot :
    def __init__(self,c,h,w) :
        self.color = c
        self.height = h
        self.weight = w
    def print_robot_info(self):
        print(f'색깔은 {self.color}')
        print(f'높이는 {self.height}')
        print(f'무게는 {self.weight}')
    def fire(self):
        print('총 발싸')
class NewRobot(Robot) :
    def __init__(self,c,h,w):
        super().__init__(c,h,w)
    def fire(self):
        print('미사일 발사')


irobot = NewRobot('red',100,1000)
irobot.print_robot_info()
irobot.fire()
