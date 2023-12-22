#Remove multiple elements from a list in Python
list=[12, 15, 3, 10]
for x in list:
    if(x%2==0):
        list.remove(x)
print(list)