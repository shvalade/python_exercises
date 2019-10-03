import operator

OperatorLookUp = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '**': operator.pow
}


def arithmetic(a, b, ch):
    try:
        return OperatorLookUp.get(ch)(a, b)
    except ZeroDivisionError:
        return 'Divide by zero! Program terminate'  # add exit(1)
    except TypeError:
        return 'Unsupported operator!'  # add exit(1)


def get_data():
    try:
        a = float(input('Enter first number: '))
        b = float(input('Enter second number: '))
    except ValueError:
        print('It is not integer!')
        exit(1)
    ch = input('Enter operator, available is : ' + OperatorLookUp.keys().__str__()[11:-2] + '\n')
    return a, b, ch


def main():
    a, b, ch = get_data()
    print(arithmetic(a, b, ch))


if __name__ == '__main__':
    main()
