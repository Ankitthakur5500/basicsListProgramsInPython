#Python Program to Swap Two Elements in a List.
List = []
while True:
    List.append(input("Enter The No.:-"))
    ans=input("Would You Like To Add More No.? y/n")
    if(ans.lower()=='n'):
        break
pos1=input("Enter First Position:-")
pos2=input("Enter Second Position:-")
def swapNumber(list,pos1,pos2):
    temp = list[pos1]
    list[pos1] = list[pos2]
    list[pos2] = temp
    return list
print(swapNumber(List,int(pos1),int(pos2)))