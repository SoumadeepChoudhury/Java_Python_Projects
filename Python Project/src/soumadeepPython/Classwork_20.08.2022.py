# Access data from nested list.
li=[[1,2],[2,3],[3,4]]
for i in li:
    for j in i:
        print(j)

# display skipping element of 1D list of 7 element.
li=[1,2,3,4,5,6,7]
for i in range(len(li)):
    if i%2==0:
        print(li[i])
    else:
        continue