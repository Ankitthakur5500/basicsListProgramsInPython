#Find sum and average of List in Python
list = [1,2,3,4,5,6,7,8,9]
sum=0
count=0
for x in list:
    sum+=x
    count+=1
avg=sum/count
print(sum)
print(int(avg))