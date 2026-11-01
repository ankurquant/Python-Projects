list = []
close2 = 0
greatest = 0

while True:
    if close2 == "no":
        break
    a = int(input("Enter no : "))
    list.append(a)
    close2 = input("Want to Insert more  [ yes/no ] :  ")
for i in range(0, len(list)):
    if list[0] > list[1] and list[0] > list[2] and list[0] > list[3]:
        greatest = list[0]

    elif list[1] > list[0] and list[1] > list[2] and list[1] > list[3]:
        greatest = list[1]

    elif list[2] > list[1] and list[2] > list[0] and list[2] > list[3]:
        greatest = list[2]

    elif list[3] > list[1] and list[3] > list[2] and list[3] > list[0]:
        greatest = list[3]
print(list)
if (
    list[0] == greatest
    and list[1] > list[2]
    and list[1] > list[3]
    and list[1] < list[0]
):
    print(f"{list[1]} is the sec greatest num. ")

elif (
    list[1] == greatest
    and list[0] > list[2]
    and list[0] > list[3]
    and list[0] < list[1]
):
    print(f"{list[0]} is the sec greatest num. ")

elif (
    list[2] == greatest
    and list[3] > list[1]
    and list[3] > list[0]
    and list[3] < list[2]
):
    print(f"{list[3]} is the sec greatest num. ")

elif (
    list[3] == greatest
    and list[2] > list[0]
    and list[2] > list[1]
    and list[2] < list[3]
):
    print(f"{list[2]} is the sec greatest num. ")
