import calendar

def month(year):
  for month in range(1, 13):
    print(calendar.month_name[month])

month(2024)