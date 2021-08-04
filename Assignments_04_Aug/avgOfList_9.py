element_list = input().split(" ")
length = len(element_list)
elements_sum = 0
for i in range(0, length):
    elements_sum = elements_sum + int(element_list[i])
print(round(elements_sum / length, 2))
