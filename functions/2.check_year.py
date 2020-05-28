month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year_arg):
    return year_arg % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year_arg, month_arg):
    if not 1 <= month_arg <= 12:
        return "Invalid Month"

    if month_arg == 2 and is_leap(year_arg):
        return 29

    return month_days[month_arg]


month = int(input("Enter Month  :  "))
year = int(input("Enter Year   :  "))

print(days_in_month(year, month))
