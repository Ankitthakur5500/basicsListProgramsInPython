#Python program to print negative numbers in a list
list1 = [12, -7, 5, 64, -14]
list2 = []
for x in list1:
    if int(x)<0:
        list2.append(x)
print(list2)