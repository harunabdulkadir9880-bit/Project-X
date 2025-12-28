calendar = str(input("please choose one EC or GC:")).upper()
date = int(input("please enter the  date:"))
month = int(input("please enter the month:"))
year = int(input("please enter the year:"))
MAX_DAYS = 30
MAX_MONTH = 12
if calendar == "GC" :
    date -= 9
    month -= 8
    year -= 8
    if date <= 0:
        date += MAX_DAYS
        month -= 1
    if month <= 0:
        month += MAX_MONTH

    if date > MAX_DAYS:
        date -= MAX_DAYS
        month += 1

    if month > MAX_MONTH:
        month -= MAX_MONTH
        year += 1

    print(f"{date}/{month}/{year} EC")
elif calendar == "EC":
    date += 9
    month += 8
    year += 8
    if month < 5:
        year += 7

    if date <= 0:
      date += MAX_DAYS
      month -= 1
    if month <= 0:
      month += MAX_MONTH

    if date > MAX_DAYS:
      date -= MAX_DAYS
      month += 1

    if month > MAX_MONTH:
       month -= MAX_MONTH
    print(f"{date}/{month}/{year} GC")


