element_list = input().split(" ")
length = len(element_list)
shortName = ""
for i in range(0, length):
    temp = element_list[i][:1]
    shortName = shortName+"."+temp
print(shortName.strip("."))