import math


def square(length):
    P = 4 * length
    S = pow(length, 2)
    diag = length * math.sqrt(2)
    res = {P, S, diag}
    return tuple(res)


def main():
    length_side = float(input('Enter square side length: '))
    res = square(length_side)
    print('Square perimetr = ' + res.__str__() + '\n')
    print('Square area = ' + '\n')
    print('Diagonal = ' + '\n')


if __name__ == '__main__':
    main()
