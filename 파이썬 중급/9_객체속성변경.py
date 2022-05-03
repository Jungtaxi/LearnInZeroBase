class NewGenerationPc :
    def __init__(self,name,cpu,memory,ssd):
        self.name = name
        self.cpu = cpu
        self.memory = memory
        self.ssd = ssd
    def doExcel(self):
        print('Excel Run!')
    def doPhotoShop(self):
        print('PhotoShop Run!')
    def printPcInfo(self):
        print(f'{self.name}의 성능')
        print(f'self.cpu : {self.cpu}')
        print(f'self.memory : {self.memory}')
        print(f'self.ssd : {self.ssd}')

myPc = NewGenerationPc('jupiter','i5','8g','259g')
myPc.printPcInfo()
print()

friendPc = NewGenerationPc('Henna','i7','16g','512g')
friendPc.printPcInfo()
print()

#내 피씨 업그레이드 하자
myPc.memory = '16g'
myPc.cpu = 'i9'
myPc.ssd = '1T'
myPc.printPcInfo()