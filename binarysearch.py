myList = [4,2,8,17,9,3,7,12,34,21]

# Condition 1: Sort it
mylist = myList.sort() 

# Declare/Initialize variables 
upperBound = len(myList) - 1
lowerBound = 0
found = False


item = int(input("Please enter item to be found"))
index = 0
while (not found) and (lowerBound != upperBound): 
    #mid point index 
    # // = integer division: means you get the integer not decimal values
    index = (upperBound + lowerBound)//2
    # compare index with item 
    if (myList[index] == item):
        found = True 
    # comapare if > or < 
    if item > myList[index]: 
        #ignore the left part of the list
        lower = index + 1 
    if item < myList[index]:
        #ignore the right part of the list
        upperBound = index - 1 

if (found):
    print(f"item found at {index}")
else: 
    print("not found")
    