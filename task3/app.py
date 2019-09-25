import math


def square(length):
    P = 4 * length
    S = length**2
    diag = length * 2**0.5
    return P, S, diag


def main():
    length_side = float(input('Enter square side length: '))
    res = square(length_side)
    print('Square perimeter = ' + res[0].__str__() + '\n')
    print('Square area = ' + res[1].__str__() + '\n')
    print('Diagonal = ' + res[2].__str__() + '\n')


if __name__ == '__main__':
    main()
