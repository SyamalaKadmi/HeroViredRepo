#Write a program that prompts the user to enter a password and validates it against a predefined correct password. 
#The program should continue to prompt for input until the correct password is entered.


password = "Sy@mu93&"

while True:
    enteredPassword = str(input("Please enter your password: "))
    if(enteredPassword == password):
        break
print("validation successful")