elements = input()
element_list = elements.split(" ")
num = len(element_list)
out = int(elements[0])
for i in range(1, num):
    out = out*int(element_list[i])
print(out)