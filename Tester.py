import datetime

dt = datetime.datetime(2021, 9, 21, 0, 0, 14)
today = datetime.datetime.now()

today_str = today.strftime('%d.%m.%Y')
print(today_str)
print(type(today_str))

dt1 = '30 Mar 21'
dt2 = 'November 15, 2001, 16:20' 
new_dt1 = datetime.datetime.strptime(dt1, '%d %b %y')
new_dt2 = datetime.datetime.strptime(dt2, '%B %d, %Y, %H:%M')

print(new_dt1)
print(type(new_dt1))

print(new_dt2)
print(type(new_dt2))