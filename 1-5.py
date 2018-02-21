num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num3 = input("Enter third number: ")
if (num1 > num2) and (num1 > num3):
 biggest = num1
if (num2 > num1) and (num2 > num3):
 biggest = num2
if (num3 > num1) and (num3 > num2):
 biggest = num3

print("The biggest number between",num1,num2,"and",num3,"is",biggest)