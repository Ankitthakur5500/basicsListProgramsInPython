#Python | Count occurrences of an element in a list
list = [1,2,3,4,5,6,7,8,9,2]
no = 2
count=0
for x in list:
    if x==no: 
     count+=1
print(count)