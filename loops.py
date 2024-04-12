# userId = int(input("Input userId: "))

# if (userId >= 5 and userId < 10):
#     print("Part of batch 5")
# else:
#     print("Not part of batch 5")
    
# #ternary operator
# eligible = "eligible" if 5<=userId<10 else "not eligible"
# print(eligible)

# #for loop
# for i in range(10):
#     print(i)

# for i in range(1, 100, 25):
#     print(i)

# for i in range(100, 1, -25):
#     print(i)

# for i in range(1,6):
#     print(13*i)

# i=1

# while(i<+5):
#     print(13*i)
#     i=i+1

# #datastructure
# #list, set, tuples, dictionary

# list1= [23,24,20,19,25,"two",67,90,[1,2,3]]
# #index
# # -1 -- backward indexing. value should be 25
# # 1 -- forward indexing. Value should be 23
# print(list1[-1])
# str = "shakulmalik1234 prerra"
# print(str[-2])

# #slicing
# print(list1[1:4])
# print(list1[1:4:1])
# print(list1[4:1:-1])
# print(str[2:6])
# print(str[7:2:-2])
# print(str[-3])
# print(list1[1:])
# print(list1[:-1])
# print(str[::-1])
# print(str[8:3:-3])

# list2 = [2,4,6,8,10,11,13,15]

# for i in list2:
#     print(i*i)

# for i in list2:
#     if(i%2!=0):
#         print(i)

# for i in list2:
#     if(i%2==0):
#         continue
#     else:
#         print(i)

# #change the values
# list1[5] = 600
# list1.append(5000)
# print(list1)
# list1.insert(3,10000)
# #remove value - pop
# list1.pop()
# #remove index value
# print(list1)
# del list1[3]
# #to remove value
# list1.remove(90)
# print(list1)

# l=[1,3,5,[3,4,5],[4,9,10]]

# for i in l:
#     if isinstance(i, list):
#         for j in i:
#             print(j)
#     else:
#         print(i)

# list3 =[]
# n= int(input["Enter the number of values to be appended: "])

# for i in range(n):
#     num = int(input["Enter the value: "])
#     list3.append[num]

# print(list3)

list4 = []

while (True):
    num = int(input("enter the value: "))
    list4.append(num)
    choice = input("do you want to add values (y/n): ")
    if(choice=='n'):
        break
print(list4)    