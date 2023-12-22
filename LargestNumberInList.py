#Python Program to Find Largest Number in a List
list=[1,2,3,4,5,6,7,8,9]
large = int(list[0])
for x in list:
    if x>large:
        large=x
print(large)