D = input()
N = input()
week_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
index = week_days.index(D)
cal = (int(N)%7)+(index-1)
if cal >7:
    cal = cal%7
expected_weekday = week_days[cal]

print(expected_weekday)
