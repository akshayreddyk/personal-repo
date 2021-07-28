num = int(input())
rows = int(input())
for i in range(0, rows):
    if i == 0:
        print(num)
        counter = 0
    else:
        num = num+1
        print(num, end=" ")
        while i > 0:
            num = num +1
            print(num, end=" ")
            i = i - 1
        print("")
