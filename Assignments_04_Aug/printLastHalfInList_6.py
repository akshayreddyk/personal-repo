num = int(input())
element_list = []
element = input()
element_list = element.split(" ")
count = num//2
temp_list = element_list[-count:]
final_list = []
for i in range(0, len(temp_list)):
    final_list.append(int(temp_list[i]))
print(final_list)