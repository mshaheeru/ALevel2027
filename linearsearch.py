# Code for Linear Search

myList = [4,2,8,17,9,3,7,12,34,21]
#COunt = 10

#enter item to search 

item = int(input("Please enter item to be found: "))
indexAt = 0
found = False

for index in range(len(myList)):
    if(myList[index] == item):
        found = True
        indexAt = index
        break

if(found):
    print("Item Found" + str(indexAt))
else:
    print("Items not found")