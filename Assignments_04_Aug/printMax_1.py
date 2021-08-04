num = int(input())
temp_list = []
for i in range(num):
    value = int(input())
    temp_list.append(value)

print(temp_list[0])
for i in range(1, len(temp_list)):
    if temp_list[i-1] > temp_list[i]:
        print(temp_list[i-1])
    else:
        print(temp_list[i])