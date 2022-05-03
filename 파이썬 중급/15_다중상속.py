class Car01 :
    def __init__(self):
        print('Car01 init 실행')
    def drive(self):
        print('drive() method called!!')
class Car02 :
    def __init__(self):
        print('Car02 init 실행')
    def turbo(self):
        print('turbo boost up!')
class Car03 :
    def __init__(self):
        print('Car03 init 실행')
    def fly(self):
        print('fly to the moon!')

class Car(Car01,Car02,Car03):
    def __init__(self):
        Car01.__init__(self)
        Car02.__init__(self)
        Car03.__init__(self)
        print('Car init 실행')

mycar = Car()
mycar.drive()
mycar.turbo()
mycar.fly()