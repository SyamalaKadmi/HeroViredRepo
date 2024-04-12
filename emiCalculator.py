p = float(input("Enter the principal amount: "))
r = float(input("Enter the annual rate of interest: "))
n = int(input("Enter the number of months: "))

r = r/(12*100) #rate of interest per month

emi = p * r * ((1+r)**n)/((1+r)**n-1)

print("Monthly EMI is: ", round(emi, 2))