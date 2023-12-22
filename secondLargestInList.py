#Python program to find second largest number in a list
list=[1,2,3,4,5,6,7,8,9]
firstLarge=int(list[0])
secondLarge=0
for x in list:
    if int(x)>firstLarge:
        secondLarge=firstLarge
        firstLarge=x
print(secondLarge)