#prime no 
fac=0
l=[]
a=len(l)
num=int(input("Enter ur no: "))

for i in range(1,num+1):
  if num%i==0:
    fac=i
    l.append(fac)
    a=len(l)
print(l)
    

    
if a==2:
  print(f"{num} is a prime no.")
else:
  print(f"{num} is not a prime no. ")

#