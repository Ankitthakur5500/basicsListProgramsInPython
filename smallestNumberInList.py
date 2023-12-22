#Python program to find smallest number in a list
list = [9,8,7,6,5,4,3,2,1]
small = int(list[0])
for x in list:
    if x < small:
        small=x
print(small)