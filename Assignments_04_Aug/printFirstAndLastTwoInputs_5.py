num = int(input())
temp_list = []
for i in range(num):
    element = int(input())
    temp_list.append(element)
element_list = []
if len(temp_list) == 2:
    element_list.append(temp_list[0])
    element_list.append(temp_list[1])
elif len(temp_list) <2:
    element_list.append(temp_list[0])
else:
    element_list.append(temp_list[0])
    element_list.append(temp_list[1])
    element_list.append(temp_list[num-2])
    element_list.append(temp_list[num-1])
print(element_list)