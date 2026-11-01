list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

list2 = []
listx = []
list3 = []
listy = []
for i in list:
    list2.append(i[0])
    listx.append(i[1])
    listy.append(i[2])
list3.append(list2)
list3.append(listx)
list3.append(listy)
print(list3)
