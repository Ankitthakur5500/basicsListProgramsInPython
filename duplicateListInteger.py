#Python | Program to print duplicates from a list of integers
list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
uniqueList = []
duplicateList = []
for x in list:
    if x not in uniqueList:
        uniqueList.append(x)
    elif x not in duplicateList :
        duplicateList.append(x)
print(duplicateList)