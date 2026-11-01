list = []
close2 = 0

while True:
    if close2 == "no":
        break
    a = int(input("Enter no : "))
    list.append(a)
    close2 = input("Want to Insert more  [ yes/no ] :  ")
for i in range(0, 4):
    if list[0] > list[1] and list[0] > list[2] and list[0] > list[3]:
        print(f"{list[0]} is largest.")
        break
    elif list[1] > list[0] and list[1] > list[2] and list[1] > list[3]:
        print(f"{list[1]} is largest.")
        break
    elif list[2] > list[1] and list[2] > list[0] and list[2] > list[3]:
        print(f"{list[2]} is largest.")
        break
    elif list[3] > list[1] and list[3] > list[2] and list[3] > list[0]:
        print(f"{list[3]} is largest.")
        break
