print("Enter a weekday: ")
D = input()
print("Enter a date: ")
N = input()

week_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

if not D in week_days:
    print("Enter valid weed day: " + str(D))

temp = None
for i, j in enumerate(week_days):
    if D == j:
        temp = i
        break
final_modulas = (int(N)-6-temp)%7
expected_weekday = week_days[final_modulas]

print(expected_weekday)

