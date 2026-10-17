num1=int(input("Enter your first number : "))
num2=int(input("Enter your second number : "))

print(type(num1))
print(id(num1))
print(id(num2))
print(hex(num1))
print(hex(num2))

r1=num1+num2
print("The result of adding two numbers is ",r1)

r2=num1*num2
print("The result of multiplying two numbers is ",r2)

if num1>num2:
    print("The result of subtracting two numbers is ",num1-num2)
    print("The result of dividing two numbers is ",num1/num2)
    
elif num1<num2:
    print("The result of subtracting two numbers is ",num2-num1)
    print("The result of dividng two numbers is ",num2/num1)