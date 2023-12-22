#Reversing a List in Python
list = [1,2,3,4,5,6,7,8,9]
start = 0
end = len(list)-1
while(start<end):
        temp=list[start]
        list[start]=list[end]
        list[end]=temp
        start+=1
        end-=1
print(list)
