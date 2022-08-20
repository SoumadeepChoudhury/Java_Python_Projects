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
# exchange element of 1st half with second half of list of 7.
li=[1,2,3,4,5,6,7]
print(li)
x1,x2,x3=li[0],li[1],li[2]
li[0],li[1],li[2]=li[4],li[5],li[6]
li[4],li[5],li[6]=x1,x2,x3
print(li)