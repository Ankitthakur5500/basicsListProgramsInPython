#Python program to count positive and negative numbers in a list
list1 = [2, -7, 5, -64, -14]
pos = 0
neg = 0
for x in list1:
    if int(x) <0:
        neg+=1
    else:
        pos+=1
print(pos)
print(neg)