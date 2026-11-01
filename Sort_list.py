list = []
close2 = 0
b = []
while True:
    a = int(input("Enter no : "))
    list.append(a)
    b = sorted(list)
    close2 = input("Want to Insert more [ yes/no ] :  ")
    if close2 == "no":
        break
    elif close2 == "yes":
        print("Ok plz")

if list == b:
    print(f"{list} is already sorted. ")

else:
    print(f"{list} is not sorted. ")
