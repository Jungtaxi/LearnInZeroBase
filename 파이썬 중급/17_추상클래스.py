from abc import ABCMeta, abstractmethod
class Parent(metaclass=ABCMeta) :
    def __init__(self):
        pass
    @abstractmethod
    def clean(self):
        print('부모 방 청소')
class Child(Parent):
    def __init__(self):
        super().__init__()
    # def clean(self):
    #     print('자녀 방 청소')

child=Child()
child.clean()