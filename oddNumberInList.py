#Python program to print odd numbers in a List
list = [1,2,3,4,5,6,7,8,9]
list2=[]
for x in list:
    if int(x)%2!=0:
        list2.append(x)
print(list2)