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
    if (not (year % 4)) and year % 100:
        return True
    return False


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


# Світлана замовляє чашки для співробітників, на яких мають бути надруковані імена.
# Напишіть будь ласка функцію, що приймає на вхід список людей, у якому кожна людина описана як словник
# ключами “name”, “surname”. А повертає структуру з іменами і кількістю чашок які потрібно замовити.
def cups(arr_dict):
    names = []
    counters = []
    for i in arr_dict:
        if i.__getitem__('name') not in names:
            names.append(i.__getitem__('name'))
            counters.append(1)
        else:
            counters[names.index(i.__getitem__('name'))] += 1
    return dict(zip(names, counters))

# Написать метод который принимет два числа a, b и возвращает все числа Фибоначчи на отрезке [a, b]
def fibo(a, b):
    x0 = 0
    x1 = 1
    res = []
    while x1 < b:
        temp = x1
        x1 += x0
        x0 = temp
        if a <= x1 <= b: res.append(x1)
    return res


# получить список всех нечётных чисел от 0 до 100
# со звёздочкой - сделайте это в одну строку
def non_pair():
    #for i in range(1, 100, 2): print(i)
    return [num for num in range(1, 100, 2)]


# напишите метод, который принимает на вход два параметра: a и b
# если тип обоих переменных (a и b) - int, вывести большее из них
# если тип обоих переменных строка - сообщить, является ли строка b подстрокой строки a
# если переменные разного типа, вывести сообщение об ошибке (любое)
def custom_compare(a,b):
    if type(a) == int and type(b) == int:
        if a < b:
            return b
        else:
            return a
    elif type(a) == str and type(b) == str:
        if a.find(b) == -1:
            return "Doesn't contains given substring"
        else:
            return 'Contains given substring!'
    return 'Error!'


# Напишіть функцію, яка приймає на вхід три параметри: початковий рік (a), кінцевий рік (b), список років (c).
# Функція має повертати список високосних років між а і b, крім вказаних у списку c
def interval_year_leap(start, end, list_year):
    if is_year_leap(start):
        pass
    else:
        start += 4 - start % 4
    res = []
    while start <= end:
        if is_year_leap(start) and start not in list_year:
            res.append(start)
        start += 4
    return res


# Найти сумму элементов массива
def array_sum(arr):
    res = 0
    for i in arr: res += i
    return res
#array_sum = sum


# Найти максимальный элемент, значение и индекс
def array_max(arr):
    res, indx = arr[0], 0
    for i in arr:
        if res < i:
            res = i
            indx = arr.index(i)
    return res, indx
#array_max = max


# Найти минимальный элемент, значение и индекс
def array_min(arr):
    res, indx = arr[0], 0
    for i in arr:
        if res > i:
            res = i
            indx = arr.index(i)
    return res, indx
#array_min = min


# Посчитать количество элементов больше нуля
def more_that_zero(arr):
    res = 0
    for i in arr:
        if i > 0: res += 1
    return res


# Прибавить к элементам массива их индекс
def add_index(arr):
    for i in range(arr.__len__()):
        arr[i] += i
    return arr


# Циклический сдвиг элементов массива на k- позиций вправо
def right_shift(arr, k):
    res = []
    for i in range(len(arr)):
        res.append(arr[i - k])
    return res


# Вывести элементы одного массива, которые не равны элементам второго массива.
def exception(arr1, arr2):
    res = []
    for i in arr1:
        if i not in arr2:
            res.append(i)
    return res


# Из двух отсортированных массивов сделать третий отсортированный, не сортируя его.
def sort(arr1, arr2):
    res = []
    i1, i2 = 0, 0
    while i1 + i2 < len(arr1) + len(arr2):
        if i1 < len(arr1) and i2 >= len(arr2):
            res.append(arr1[i1])
            i1 += 1
        elif i1 >= len(arr1) and i2 < len(arr2):
            res.append(arr2[i2])
            i2 += 1
        else:
            if arr1[i1] < arr2[i2]:
                res.append(arr1[i1])
                i1 += 1
            else:
                res.append(arr2[i2])
                i2 += 1
    return res


def main():
    #list1 = [34, 22, 55, 1]
    #print(sort([22, 33, 34, 39, 54], [23, 33, 39, 50, 59]))
    #print(right_shift([1, 2, 3, 4, 5, 6], 4))
    names = (
        {'name': 'Vasiliy', 'surname': 'Vasilyevich'},
        {'name': 'Ivan', 'surname': 'Ivanov'},
        {'name': 'Vladimir', 'surname': 'Ivanov'},
        {'name': 'Ivan', 'surname': 'Hills'},
        {'name': 'Vladimir', 'surname': 'Ivanov'},
        {'name': 'Vladimir', 'surname': 'Ivanov'},
        {'name': 'Vladimir', 'surname': 'Ivanov'},
        {'name': 'Vladimir', 'surname': 'Ivanov'},
        {'name': 'Vladimir', 'surname': 'Ivanov'}
    )
    print(cups(names))


if __name__ == '__main__':
    main()
