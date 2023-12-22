#Python program to count Even and Odd numbers in a List
list1 = [2, 7, 5, 64, 14]
odd = 0
even = 0
for x in list1:
    if int(x)%2==0:
        even+=1
    else:
        odd+=1
print("even="+str(even))
print("odd="+str(odd))
