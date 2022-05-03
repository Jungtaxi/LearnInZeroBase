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
        print()

pc1 = NewGenerationPc('jupiter','i5','8g','259g')
pc2 = NewGenerationPc('Henna','i7','16g','512g')
pc3 = pc1

pc1.printPcInfo()
pc2.printPcInfo()
pc3.printPcInfo()

pc3.name = 'this is pc3'
pc3.printPcInfo()
pc1.printPcInfo()