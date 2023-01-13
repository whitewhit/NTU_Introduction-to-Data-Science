from datetime import datetime
from dateutil.relativedelta import relativedelta

def n_times_day(bday1, bday2, n=2):

    if bday2.year > bday1.year:
        y = bday2.year
        delta = bday2 - bday1
        cday = bday2 + (n-1)*delta
    else:
        y = bday1.year
        delta = bday1 - bday2
        cday = bday1 + (n-1)*delta

    dday = datetime(day=1, month=1, year = y)
    delta = relativedelta(years=+1)
    while True:
        dday+=delta
        d1 = dday.year - bday1.year
        d2 = dday.year - bday2.year
        if (d1 == n*d2):
            break
        elif(d2 == n*d1):
            break

    return cday, dday


def main():

    print("Lab03 B-1")
    now = datetime.now()
    print("Today's date and the day of the week:")
    print(now)
    print(now.strftime('%A'))

    # Your output should be like:
    # 2020-08-03 20:19:19.806211
    # Monday

    print("Lab03 B-2")
    s = input('Enter your birthday in mm/dd/yyyy format: ') #'1/15/1997'
    print("Time until your next birthday and your current age are:")

    format_string = "%m/%d/%Y"
    your_b_day = datetime.strptime(s, format_string)
    years_old = 0
    delta = relativedelta(years=+1)
    while your_b_day < now:
        your_b_day += delta
        years_old+=1
    print(your_b_day - now)
    print(years_old - 1)

    # Your output should be like:
    # 280 days, 3:40:40.1937891
    # 22

    print("Lab03 B-3")
    print("For people born on these dates:")
    bday1 = datetime(day=15, month=1, year=1997)
    bday2 = datetime(day=11, month=10, year=2003)
    print("Double Day is")

    y = bday2.year
    cday = datetime(day=1, month=1, year = y)
    while True:
        cday+=delta
        d1 = cday.year - bday1.year
        d2 = cday.year - bday2.year
        if (d1 == 2*d2):
            print(cday, '(for years old)')
            break

    cday = bday2 - bday1
    print(bday2 + cday, '(for days)')

    # Your output should be like:
    # 2020-01-01 00:00:00 (this is not the correct answer!)

    print("Lab03 B-4")
    use_day, use_year= n_times_day(bday1, bday2, n=3)
    print("Triple Day is ", use_year, "(for years old)")
    print("Triple Day is ", use_day, "(for days)")

if __name__ == '__main__':
    main()