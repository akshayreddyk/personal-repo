element_list = input().split(" ")
final_list = []
length = len(element_list)
for i in range(length):
    final_list.append(int(element_list[i]))
final_list.sort()
print(int(final_list[length-1]))