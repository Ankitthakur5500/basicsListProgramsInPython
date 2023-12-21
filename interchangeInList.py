#Python program to interchange first and last elements in a list
def interChangeList(list):
    size=len(list)
    temp = list[0]
    list[0]=list[size-1]
    list[size-1]=temp
    return list
# list = [1,2,3,4,5]
list = []
while True:
        list.append(input("Enter The Number:"))
        ans = input("would you like to enter more no. ? y/n:")
        if ans.lower() == 'n':
              break
print(interChangeList(list))
