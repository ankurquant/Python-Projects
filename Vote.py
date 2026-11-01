
name=input("enter name: ")
age=int(input("enter ur age: "))
has_lisence=True

print(f"Hi there {name}  , Have a great  day !!")

if age>=18 and has_lisence:
  print("you r eligible for voting !")
  
elif age>=18 or not has_lisence:
  print("sorry! make ur lisence first " )

else:
  print("sorry u r not eligible ! ")