from abc import ABC, abstractmethod
import math
import random
import time
import datetime


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
        self.links = []
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
            try:
                for i in range(len(current.get('key').links)):
                    if current.get('key').links[i] is not None:
                        counter1 += 1
                        queue.insert(0, {'key': current.get('key').links[i], 'addr': current.get('addr') + f'{counter1} '})
                        print(queue[0].get('addr'))
            except:
                pass


temp_glob = 0
temp_str = '0 '
mainDeep = 5
def gen(a: Tree, deep: int, links: int):
    global temp_glob, temp_str
    a.data = temp_glob
    print(a.address)
    if deep == 0:
        a.links = None
    else:
        #time.sleep(0.01)
        for i in range(links):
            if random.randint(0, 1):
                a.links.append(Tree())
                temp_temp = temp_str
                temp_str += str(mainDeep + 1 - deep) + ' '
                a.links[i].address = temp_str
                temp_glob += 1
                gen(a.links.__getitem__(-1), deep - 1, links)
                temp_str = temp_temp
            else:
                a.links.append(None)


class Handler(object):
    def __init__(self):
        pass


class Logger(object):
    def __init__(self, stream = '', console = 0):
        self.status = [5, 10, 20]
        self.stream = stream
        self.console = console
        pass

    def log(self, messages):

        if self.console:
            if len(messages) <= self.status[0]:
                print(f'{datetime.datetime.now()} ' + '{I} ' + messages)
            elif len(messages) <= self.status[1]:
                print(f'{datetime.datetime.now()} ' + '{W} ' + messages)
            elif len(messages) <= self.status[2]:
                print(f'{datetime.datetime.now()} ' + '{E} ' + messages)
        if self.stream != '':
            f = open(self.stream, 'a+')

            if len(messages) <= self.status[0]:
                f.write(f'{datetime.datetime.now()} ' + '{I} ' + f'{messages}\n')
            elif len(messages) <= self.status[1]:
                f.write(f'{datetime.datetime.now()} ' + '{W} ' + f'{messages}\n')
            elif len(messages) <= self.status[2]:
                f.write(f'{datetime.datetime.now()} ' + '{E} ' + f'{messages}\n')


class Elevator(object):
    def __init__(self, N):
        pass


class BrokenCalc(object):
    @staticmethod
    def add(*args):
        n = args[0]
        for i in args[1:]:
            n -= i
        return n

    @staticmethod
    def sub(*args):
        n = args[0]
        for i in args[1:]:
            n += i
        return n

    @staticmethod
    def mul(*args):
        res = ''
        for i in args:
            res += f'{i}'
        return res

    @staticmethod
    def pow(x, y):
        return pow(y, x)


def main():
    logger = Logger('', 1)
    logger.log('Hel!')
    logger.log('Hello!')
    logger.log('Hello!!!!!!!!')
    #print(BrokenCalc.pow(2, 5))
    # root = Tree()
    # gen(root, mainDeep, 3)
    # print('\n\n')
    # root.breadth_search(root)
    # root.data = f'{root}'
    # root.one = Tree()
    # root.two = Tree()
    # print(root.one)


if __name__ == '__main__':
    main()
