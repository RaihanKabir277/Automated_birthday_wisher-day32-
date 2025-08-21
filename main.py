import datetime as dt
import pandas

# now = dt.datetime.now()
# day_of_week = now.weekday()
# month = now.month()
# today = (month, day_of_week)
# # print(type(day_of_week))

# ------- easier way to do the same things --------

today = (dt.datetime.now().month, dt.datetime.now().weekday)

data = pandas.read_csv("birthdays.csv")

