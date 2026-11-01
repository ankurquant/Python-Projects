# 1.

"""num = 5

for i in range(6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()"""

# 2.

"""num=int(input("Enter no : "))

for i in range(1,num+1):
    if num%i==0:
        print(f"Factors : {i}")"""
# 3.

"""n=int(input("Enter no : "))
l=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
if len(l) ==2:
    print(" Prime no.")
else:
    print("Not a prime no. ")"""
# 4.

"""b=0
n=int(input("Enter no : "))
for i in range(1,n+1):
    b+=1/i
    
print(b)"""

# 5.

"""n=int(input("Enter no : "))
l=[]
b=0
for i in range(1,n):
    if n%i==0:
        l.append(i)
for j in l:
    b+=j
if b==n:
    print(f"{n} is a perfect no. ")
else:
    print(f"{n} is not a  perfect no. ")"""

# 6.
"""p=int(input("Enter starting no : "))
for i in range(5,0,-1):
    for m in range(i,0,-1):
        print(p,end=" ")
        p-=1
    print()"""
# 7.
"""def even_num(n):
    for i in range(1,n+1):
        if i%2==0:
            print (i)
even_num(10)"""
# 8.
