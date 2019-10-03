libSeason = {
    0: 'winter',
    1: 'spring',
    2: 'summer',
    3: 'autumn',
    4: 'winter'
}


def season(num):
    print(libSeason.get(num // 3))
    pass


def main():
    num = int(input('input num of month: '))
    season(num)
    pass


if __name__ == '__main__':
    main()
