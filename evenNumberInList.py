#Python program to print even numbers in a list
list1=[1,2,3,4,5,6,7,8,9]
list2=[]
for x in list1:
    if int(x)%2==0:
        list2.append(x)
print(list2)