my_list = [1,2,3,3]
count = {}

for  x in my_list:
    if x in count:
        count[x] += 1

    else:
        count[x] = 1

print(count)

