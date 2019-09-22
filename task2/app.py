def is_year_leap(year):
    if year % 4:
        return False
    else:
        return True


def main():
    input_year = int(input('Enter year: '))
    print(is_year_leap(input_year))


if __name__ == '__main__':
    main()
