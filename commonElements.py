"""
Write a Python program that finds and displays the common elements between two sets.

Requirements

Prompt the user to enter elements for two sets, separated by commas.
Create sets from the user input.
Find and display the common elements present in both sets.
If there are no common elements, display a message indicating no common elements.
"""
set1 = (input("Enter elements of set1 (comma separated): "))
set2 = (input("Enter elements of set2 (comma separated): "))

print(set1)
print(set2)
set1 = set1.split(',')
set2 = set2.split(',')
a_set1 = set(set1)
b_set2 = set(set2)

print("Set 1: ", a_set1)
print("Set 2: ", b_set2)

if(a_set1 & b_set2):
    print("Common Elements: ", a_set1 & b_set2)
else:
    print("No common elements")