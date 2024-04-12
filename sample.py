def sum(x,y):
    result = x+y
    print(f"the sum of {x} and {y} is {result}")
def sub(x,y):
    result = x-y
    print(f"the subtraction of {x} and {y} is {result}")
def multiply(x,y):
    result = x*y
    print(f"the multiplication of {x} and {y} is {result}")
def divide(x,y):
    result = x//y
    print(f"the division of {x} and {y} is {result}")
def remainder(x,y):
    result = x%y
    print(f"the remainder of {x} and {y} is {result}")

name= input("please tell your name:- ")
print("hello",name)

num1= float(input("enter the first number: "))
num2= float(input("enter the second number: "))

choice = int(input("""Please select the operation you want to perform: 
               Press 1 for addition
               Press 2 for Subtraction
               Press 3 for multiplication
               Press 4 for division
               """))

if (choice == 1):
    sum(num1,num2)
elif(choice==2):
    sub(num1,num2)
elif(choice==3):
    multiply(num1,num2)
elif(choice==4):
    divide(num1,num2)
elif(choice==5):
    remainder(num1,num2)
else:
    print("Incorrect input")
