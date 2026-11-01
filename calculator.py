def calculator(a, b, op):
    try:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b
        elif op == "//":
            return a // b
        elif op == "**":
            return a**b
        else:
            return None
    except ZeroDivisionError:
        return None


a = int(input("Enter 1st no : "))
b = int(input("Enter 2st no : "))
op = input("Enter operator : ")
x = calculator(a, b, op)
if x == None:
    print("Invalid")
else:
    print(x)
