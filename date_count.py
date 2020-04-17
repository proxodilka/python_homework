import datetime

s = input().split()
d = datetime.date(int(s[0]), int(s[1]), int(s[2]))+datetime.timedelta(int(input()))
print(d.year, d.month, d.day)
