# 4.3 The datetime Module
import datetime as dt


# 4.4. The datetime Class
eg_1 = dt.datetime(2000, 1, 1)  # instantiate an object with a date, representing January 1, 2000
print(eg_1)
eg_2 = dt.datetime(1985, 3, 13, 21, 26, 2)  # instantiate an object with both a date and a time
print(eg_2)
eg_3 = dt.datetime(1998, 7, 7, 8, 39)  # we can specify some but not all time arguments (no arg for second)
print(eg_3)
print()


# 4.5 Using strptime to Parse Strings as Dates
strdate1 = "24/12/1984"  # day/month/year format
date1 = dt.datetime.strptime(strdate1, "%d/%m/%Y")
print(type(date1))
print(date1)
strdate2 = "12-24-1984"  # month/day/year format
date2 = dt.datetime.strptime(strdate2, "%m-%d-%Y")
print(date2)
print()


# 4.6 Using strftime to format dates
dtobj = dt.datetime(1984, 12, 24)
print(dtobj)
dtf1 = dtobj.strftime("%d/%m/%Y")  # dat/month/4-year format
print(dtf1)
dtf2 = dtobj.strftime("%B %d, %Y")  # month-word day, 4-year format
print(dtf2)
dtf3 = dtobj.strftime("%A %B %d at %I:%M %p")  # day-word month-word day at 12-hour:minute:AM or PM
print(dtf3)
print()


# 4.7 The time Class
two_thirty = dt.time(14, 30)
print(two_thirty)
five_sec_after_8am = dt.time(8, 0, 5)
print(five_sec_after_8am)
# create a time object from a datetime object
jfk_shot_dt = dt.datetime(1963, 11, 22, 12, 30)  # 'datetime' object
print(jfk_shot_dt)
jfk_shot_t = jfk_shot_dt.time()  # convert to 'time' object
print(jfk_shot_t)
# parsing time in string form
time_str = "8:00"  # time in string form
time_dt = dt.datetime.strptime(time_str, "%H:%M")  # parse string to 'datetime' object
print(time_dt)
time_t = time_dt.time()  # convert 'datetime' object to 'time' object
print(time_t)
print()


# 4.8 Comparing time Objects
t1 = dt.time(15, 30)
t2 = dt.time(10, 45)
print(t1 > t2)

times = [dt.time(23, 30), dt.time(14, 45), dt.time(8, 0)]
print(min(times))
print(max(times))
print()


# 4.9 Calculations with Dates and Times
dt1 = dt.datetime(2022, 4, 14)
dt2 = dt.datetime(2022, 3, 29)

# print(dt1 + dt2)  # TypeError
diff = dt1 - dt2
print(diff)
print(dt2 - dt1)
print(type(diff))  # timedelta object

two_days = dt.timedelta(2)
print(two_days)
three_weeks = dt.timedelta(weeks=3)
print(three_weeks)
d1 = dt.date(1963, 2, 21)
d1_plus_1wk = d1 + dt.timedelta(weeks=1)
print(d1_plus_1wk)

dt_1 = dt.datetime(1981, 1, 31)
dt_2 = dt.datetime(1984, 6, 28)
dt_3 = dt.datetime(2016, 5, 24)
dt_4 = dt.datetime(2001, 1, 1, 8, 24, 13)
answer_1 = dt_2 - dt_1
print(dt_2, '-', dt_1, '=', answer_1)
answer_2 = dt_3 + dt.timedelta(days=56)
print(dt_3, '+ 56 days =', answer_2)
answer_3 = dt_4 - dt.timedelta(seconds=3600)
print(dt_4, '- 3600 seconds =', answer_3)


# 4.10 Summarizing Appointment Lengths
length_counts = {dt.timedelta(minutes=15): 21, dt.timedelta(hours=3): 1, dt.timedelta(seconds=45): 15}
min_length = min(length_counts)
print(min_length)
max_length = max(length_counts)
print(max_length)
