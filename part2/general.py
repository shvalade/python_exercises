from abc import ABC, abstractmethod
import math
import random
import time


class Figure(ABC):
    @abstractmethod
    def area(self):
        print('Area!')

    @abstractmethod
    def perimeter(self):
        print('Perimeter!')


class Ellipse(Figure):
    def __init__(self, semi_major_axis: float, semi_minor_axis: float):
        if semi_major_axis >= semi_minor_axis:
            self.a = semi_major_axis
            self.b = semi_minor_axis
        else:
            print('Major axis less then minor axis! Values are swap')
            self.a = semi_minor_axis
            self.b = semi_major_axis

    def area(self):
        return math.pi * self.a * self.b

    def perimeter(self):
        a = self.a
        b = self.b
        return math.pi*(a+b)*(1+((3*((a-b) / (a+b))**2) / (10+math.sqrt(4 - 3*((a-b) / (a+b))**2))))
        # формула Рамануджана


class Circle(Ellipse):
    def __init__(self, radius: float):
        super().__init__(radius, radius)
        self.a = radius
        self.b = radius


class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float):
        if a > 0 and b > 0 and c > 0 and not(a+b <= c or a+c <= b or b+c <= a):
            self.a = a
            self.b = b
            self.c = c
        else:
            print('Wrong parameters!')
            exit(0)

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

    def perimeter(self):
        return self.a + self.b + self.c


class IsoscelesTriangle(Triangle):
    def __init__(self, isosceles: float, c: float):
        super().__init__(isosceles, isosceles, c)


class EquilateralTriangle(Triangle):
    def __init__(self, a: float):
        super().__init__(a, a, a)


class Rectangle(Figure):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def area(self):
        return self.a*self.b

    def perimeter(self):
        return 2*self.a + 2*self.b


class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side)


res_str = '0 '
counter = 1
class Tree(object):

    def __init__(self):
        self.one = None
        self.two = None
        self.data = None
        self.address = None

    @staticmethod
    def depth_search(self):
        a = self
        global res_str, counter
        # temp_glob += 1
        if a.one is not None:
            temp = res_str
            res_str += str(counter) + ' '
            counter += 1
            print(res_str)
            a.depth_search(a.one)
            res_str = temp
        if a.two is not None:
            temp = res_str
            res_str += str(counter) + ' '
            counter += 1
            print(res_str)
            a.depth_search(a.two)
            res_str = temp

    @staticmethod
    def breadth_search(self):
        queue = list()
        queue.append({'key': self, 'addr': '0 '})
        counter1 = 0
        while queue:
            current = queue.pop()
            if current.get('key').one is not None:
                counter1 += 1
                queue.insert(0, {'key': current.get('key').one, 'addr': current.get('addr') + f'{counter1} '})
                print(queue[0].get('addr'))
            if current.get('key').two is not None:
                counter1 += 1
                queue.insert(0, {'key': current.get('key').two, 'addr': current.get('addr') + f'{counter1} '})
                print(queue[0].get('addr'))


temp_glob = 0
temp_str = '0 '
def gen(a: Tree, deep: int):
    global temp_glob, temp_str
    #temp_glob += 1

    a.data = temp_glob
    print(a.address)
    if deep == 0:
        a.one = None
        a.two = None

    else:
        time.sleep(0.09)
        if int(random.random()*1000) % 2:
            a.one = Tree()
            temp_temp = temp_str
            temp_str += str(7-deep) + ' '
            a.one.address = temp_str
            temp_glob += 1
            gen(a.one, deep-1)
            temp_str = temp_temp

        else:
            a.one = None
        time.sleep(0.11)
        if int(random.random()*1000) % 2:
            a.two = Tree()
            temp_temp = temp_str
            temp_str += str(7-deep) + ' '
            a.two.address = temp_str
            temp_glob += 1
            gen(a.two, deep-1)
            temp_str = temp_temp
        else:
            a.two = None
        # a.two = Tree()
        # gen(a.two, deep-1)


class BrokenCalc(object):
    pass


def main():
    root = Tree()
    gen(root, 6)
    print('\n\n')
    root.breadth_search(root)
    # root.data = f'{root}'
    # root.one = Tree()
    # root.two = Tree()
    # print(root.one)


if __name__ == '__main__':
    main()