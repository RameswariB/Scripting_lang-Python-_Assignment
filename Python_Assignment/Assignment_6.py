import math


class Quadrilateral:
    def __init__(self,cord1,cord2,cord3,cord4):
        self.cord1=cord1
        self.cord2=cord2
        self.cord3=cord3
        self.cord4=cord4

class Parallelogram(Quadrilateral):
    def __init__(self,cord1,cord2):
        Quadrilateral.__init__(self,cord1,cord2,0,0)
        self.cal_Area()
        self.draw_Parallelogram()

    def cal_Area(self):
        print('Area of Sqaure is :',math.pow(self.cord2, 2).__str__())
        print('Area of Rectangle  is :',self.cord2*3)
        print('Perimeter of Sqaure is :',self.cord2*4)
        print('Perimeter of Rectangle  is :',(2*self.cord2)+(2*self.cord2))

    def draw_Parallelogram(self):
        for i in range(self.cord2):
            if (i == 0) or (i == ((self.cord2)-1)):
                print(i*" "+(self.cord2)*"*")
            else:
                print(i*" "+"*"+((self.cord2)-2)*" "+"*")


class Square(Parallelogram):
    def __init__(self,cord1,cord2):
        Parallelogram.__init__(self,cord1,cord2)
        self.draw_Square()

    def draw_Square(self):
        print('\n=============================print Square============================\n')
        for i in range(self.cord1, self.cord2):
            for j in range(self.cord1, self.cord2):
                if j <= i:
                    print('*', end=' ')
                else:
                    print('*', end=' ')
            print()

class Rectangle(Square):
    def __init__(self,cord1,cord2):
        Square.__init__(self,cord1,cord2)
        self.draw_Rectangle()

    def draw_Rectangle(self):
        print('\n=============================print Rectangle============================\n')
        for i in range(self.cord1, self.cord2):
            for j in range(self.cord1, self.cord2*2):
                if j <= i:
                    print('*', end=' ')
                else:
                    print('*', end=' ')
            print()


print('=================================print Rectangle=====================================')
x1=int(input('Enter first Cord ? '))
x2=int(input('Enter Second Cord ? '))
r1=Rectangle(x1,x2)



