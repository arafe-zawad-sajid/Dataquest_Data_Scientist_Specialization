# 4.1 Introduction
from csv import reader

fhand = open('potus_visitors_2015.csv')
file = reader(fhand)
dataset = list(file)
header = dataset[0]
potus = dataset[1:]
# ---

# 4.5 Using Strptime to Parse Strings as Dates
import datetime as dt

date_format = '%m/%d/%y %H:%M'
for row in potus:
    appt_start_date = row[2]
    row[2] = dt.datetime.strptime(appt_start_date, date_format)
# ---

# 4.6 Using Strftime to format dates
visitors_per_month = {}
for row in potus:
    appt_start_date = row[2]
    month_year = appt_start_date.strftime('%B, %Y')
    if month_year not in visitors_per_month:
        visitors_per_month[month_year] = 1
    else:
        visitors_per_month[month_year] += 1
print(visitors_per_month)
# ---

# 4.7 The time Class
appt_times = []
for row in potus:
    appt_start_dt = row[2]
    appt_start_t = appt_start_dt.time()
    appt_times.append(appt_start_t)
# ---

# 4.8 Comparing time Objects
min_time = min(appt_times)
max_time = max(appt_times)
print('earliest appointment time', min_time, ', latest appointment time',max_time)
# ---

# 4.10 Summarizing Appointment Lengths
for row in potus:
    appt_end_date = row[3]
    row[3] = dt.datetime.strptime(appt_end_date, date_format)

appt_lengths = {}
for row in potus:
    appt_start_date = row[2]
    appt_end_date = row[3]
    length = appt_end_date - appt_start_date
    if length not in appt_lengths:
        appt_lengths[length] = 1
    else:
        appt_lengths[length] += 1

min_length = min(appt_lengths)
max_length = max(appt_lengths)
print('min meeting length', min_length, ', max meeting length', max_length)
