class NormalCar:
    def drive(self):
        print('전진한다.')
    def back(self):
        print('후진한다.')

class TurboCar(NormalCar):            #터보 자동차는 일반 자동차의 기능을 다 쓸 수 있다.
    def turbo(self) : 
        print('터보모드!!!')

print('터보차는 다음의 기능이 있습니다.')
turbo1 = TurboCar()
turbo1.turbo()
turbo1.drive()
turbo1.back()
print()


class FlyingCar(TurboCar):
    def fly(self):
        print('난다!!!!')

print('하늘을 나는 차는 터보차에 날개를 단 차입니다.')
flycar1 = FlyingCar()
flycar1.drive()
flycar1.back()
flycar1.turbo()
flycar1.fly()