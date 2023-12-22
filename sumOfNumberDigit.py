#Python | Sum of number digits in List
list1 = [11,12,13,14,15,16,17,18]
list2 = []
for x in list1:
    sum=0
    for a in str(x):
        sum+=int(a)
    list2.append(sum)
print(list2)