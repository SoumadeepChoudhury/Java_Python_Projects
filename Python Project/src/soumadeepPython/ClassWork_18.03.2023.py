# Given list is [1,2,3]. Convert into 2D list in decresing order.
lis:list=[1,2,3]
newList:list=[]
for i in range(len(lis)):
    arrangeList:list=[]
    for j in range(len(lis)):
        if j>i:
            arrangeList.append(0)
            continue
        arrangeList.append(lis[j])
    newList.append(arrangeList)
newList=newList[::-1]
print(newList)
