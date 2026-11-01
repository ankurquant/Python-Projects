list = []
positive = []
negative = []
close2 = 0

while True:
    if close2 == "no":
        break
    a = int(input("Enter no : "))
    list.append(a)
    close2 = input("Want to Insert more  [ yes/no ] :  ")

for i in range(0, len(list)):
    if list[i] >= 0:
        positive.append(list[i])
    else:
        negative.append(list[i])

print(f"Positive : {positive}")
print(f"Negative : {negative}")
