# Write a program that calculates the sum of all numbers from 1 to a given positive integer n
number = int(input("Enter the number: "))

count = 0
for i in range(1,number+1):
    count = count + i
print(f"The sum of all numbers from 1 to {number} is {count}")