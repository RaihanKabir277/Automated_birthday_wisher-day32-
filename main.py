import datetime as dt
import pandas
import random
# now = dt.datetime.now()
# day_of_week = now.weekday()
# month = now.month()
# today = (month, day_of_week)
# # print(type(day_of_week))

# ------- easier way to do the same things --------

today = (dt.datetime.now().month, dt.datetime.now().day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,4)}.txt"
    with open(file_path) as file:
        contents = file.read()
        contents.replace("[NAME]", person["name"])
    print(contents)

