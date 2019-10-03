def is_year_leap(year):
    if not (year % 400):
        return True
    if not (year % 4) and year % 100:
        return True


def main():
    input_year = int(input('Enter year: '))
    print(is_year_leap(input_year))


if __name__ == '__main__':
    main()
