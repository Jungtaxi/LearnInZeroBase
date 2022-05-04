class TriangleArea :
    def __init__(self,w,h):
        self.width = w
        self.height = h
    def print_info(self):
        print(f'너비는 {self.width}, 높이는 {self.height}')
    def getArea(self):
        return round(self.width*self.height/2,2)
class UpgradeTriangleArea(TriangleArea):
    def __init__(self, w, h):
        super().__init__(w, h)
    def getArea(self):
        print(str(super().getArea())+'㎠')

triangle = UpgradeTriangleArea(4,6)
triangle.print_info()
triangle.getArea()
