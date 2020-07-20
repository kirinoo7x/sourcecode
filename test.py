def monthRe(monthCK, day, month, year):
    if day <= monthCK:
        print(day)
        print(month)
        print(year)
    else:
        month += 1
        if month <= 12:
            day = (day - monthCK)
            print(monthCK)
            print(day)
            print(month)
            print(year)
        else:
            year += 1
            month = month - 12
            day = (day - monthCK)
            print(day)
            print(month)
            print(year)

if __name__ == '__main__':
    day = int(input("d:: "))
    month = int(input("m:: "))
    year = int(input("y:: "))

    day += 17

    if month == 4 or month == 6 or month ==9 or month == 11 :
        monthCK = 30
        monthRe(monthCK, day, month, year)
    if month == 2:
        if year%4 == 0:
            monthCK = 29
            monthRe(monthCK, day, month, year)
        else:
            monthCK = 28
            monthRe(monthCK, day, month, year)
    else:
        monthCK = 31
        monthRe(monthCK, day, month, year)
