# Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий -
# операция, которая должна быть произведена над ними. Если третий аргумент +, сложить
# их; если --, то вычесть; * — умножить; / — разделить (первое на второе). В остальных
# случаях вернуть строку “Неизвестная операция”.
import operator


def arithmetic(a, b, ch):
    operator_look_up = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '**': operator.pow
    }
    try:
        return operator_look_up.get(ch)(a, b)
    except ZeroDivisionError:
        return 'Divide by zero! Program terminate'  # add exit(1)
    except TypeError:
        return 'Unknown operator!'  # add exit(1)


# Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую
# True, если год високосный, и False иначе.
def is_year_leap(year):
    if not (year % 400):
        return True
    if not (year % 4) and year % 100:
        return True


# Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата.
def square(length):
    P = 4 * length
    S = length ** 2
    diag = length * 2 ** 0.5
    return P, S, diag


# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года,
# которому этот месяц принадлежит (зима, весна, лето или осень).
def season(num):
    lib_season = {
        0: 'winter',
        1: 'spring',
        2: 'summer',
        3: 'autumn',
        4: 'winter'
    }
    return lib_season.get(num // 3)


# Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых (каждый год размер его вклада
# увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
# Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.
def bank(a, years):
    for i in range(years):
        a *= 1.1
    return a


# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True,
# если оно простое, и False - иначе
def is_prime(numb):
    if numb == 1:
        return False
    for i in range(2, numb // 2):
        if not (numb % i):
            return False
    return True


# Написать функцию date, принимающую 3 аргумента — день, месяц и год. Вернуть True,
# если такая дата есть в нашем календаре, и False иначе.
def date(day, month, year):
    month_days = {
        1: 31,
        2: 29 if is_year_leap(year) else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    if 1 <= month <= 12 and 1 <= day <= month_days.get(month):
        return True
    return False


# XOR-шифрование
# def XOR_cipher(string, key):
#     res = ''
#     some = 0
#     for i in range(len(string)):
#         res += chr(ord(string[i]) ^ ord(key[i - some]))
#         if i == some + len(key) - 1:
#             some = i + 1
#     return res

def XOR_cipher(string, key):
    if len(string) % len(key):
        key *= len(string) // len(key) + 1
    res = ''
    for a, b in zip(string, key):
        res += chr(ord(a) ^ ord(b))
    return res


XOR_uncipher = XOR_cipher


def main():
    cripted = XOR_cipher('Hello World!))))', 'qwerty123456789')
    print(cripted)
    decripted = XOR_uncipher(cripted, 'qwerty123456789')
    print(decripted)
    pass


if __name__ == '__main__':
    main()
