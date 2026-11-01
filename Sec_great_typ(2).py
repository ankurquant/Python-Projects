list = []
close2 = 0
greatest = 0


while True:
    a = int(input("Enter no : "))
    list.append(a)
    close2 = input("Want to Insert more [ yes/no ] :  ")

    if close2 == "no":
        break
    elif close2 == "yes":
        print("Ok plz")


list.sort()
print(list)
if len(list) > 1:
    print(f"{list[len(list) - 2]} is the sec greatest no. ")
else:
    print(f"{list[0]} is the greatest num .")
