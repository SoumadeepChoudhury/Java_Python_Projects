# WAP TO FIND THE WORD USED MINIMUM NUMBER OF TIMES IN A GIVEN FILE...
txt_list = open(
    input("Enter file name with extension and directory: ")).read().split(' ')
temp, count_, word = 0, txt_list.count(txt_list[0]), txt_list[0]
temp_list = list(txt_list[0])
for i in range(1, len(txt_list)):
    if txt_list[i] in temp_list:
        continue
    temp = txt_list.count(txt_list[i])
    temp_list.append(txt_list[i]) if temp > 1 else None
    if temp < count_:
        count_ = temp
        word = txt_list[i]
print(word)
