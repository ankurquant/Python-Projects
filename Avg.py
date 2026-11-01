list = []
close2 = 0
avg = 0
while True:
    if close2 == "no":
        break
    a = int(input("Enter no : "))
    list.append(a)
    close2 = input("Want to Insert more  [ yes/no ] :  ")

for i in list:
    avg += i

print(avg / len(list))
