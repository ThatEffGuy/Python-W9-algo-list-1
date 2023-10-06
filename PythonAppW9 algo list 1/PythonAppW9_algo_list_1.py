aStrList = ["a", "b", "c", "d", "e",]
aNumList = [1, 2 ,3 ,4 ,5]


#Iterate groups
#Method 1
for item in aStrList:
    print("str item: " + item)

for item in aNumList:
    print("num item: " + str(item))

#Method 2
for index in range(0, len(aStrList)):
    print("str item: "+ aStrList[index] )

for index in range(0, len(aNumList)):
    print("num item:"+ str(aNumList[index]))


#Method 3 for numbers

for item in aNumList:
    print ("Meth 3 Num item", item)

