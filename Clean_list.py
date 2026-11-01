list = [1, [2, [3, 4], 5], 6, [7]]
l1 = []
l2 = []
l3 = []
l4 = []


l1.append(list[0])
l1.append(list[2])
l1.append(list[3][0])
l1.append(list[1][0])
l1.append(list[1][2])
l2.append(list[1][1])
l3.append(l2[0][0])
l3.append(l2[0][1])
l1.append(l3[0])
l1.append(l3[1])
l4 = sorted(l1)
print(l4)
