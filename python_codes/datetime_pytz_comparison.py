import datetime
import pytz

print("now - pytz.timezone('Asia/Taipei')")
now_date_time = datetime.datetime.now(pytz.timezone('Asia/Taipei'))
print(now_date_time)

# print("now - pure now()")
# now_date_time = datetime.datetime.now()
# now_date_time = datetime.datetime.now(tz=pytz.UTC)
# print(now_date_time)

# print("now with utc")
# now_date_time = datetime.datetime.now(datetime.timezone.utc)
# print(now_date_time)

print("now with utc 2")
# utc_dt = datetime.datetime(2023, 11, 30, 3, 51, 26, tzinfo=datetime.timezone.utc)
utc_dt = datetime.datetime(2023, 12, 7, 3, 51, 26, tzinfo=pytz.timezone('Asia/Taipei'))
print(utc_dt)

print(now_date_time > utc_dt)
time_diff = now_date_time - utc_dt
print(time_diff.days)

# ---------------------
# Result
# ---------------------
# now - pytz.timezone('Asia/Taipei')
# 2024-01-07 17:32:20.673644+08:00
# now with utc 2
# 2023-12-07 03:51:26+08:06
# True
# 31
