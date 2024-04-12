# List - ordered, changeable(mutable), duplicate values
# Tuple - ordered, unchangeable(immutable), duplicate values
# set - unordered, immutable (u can go ahead and add items and remove items)

a= (1,2,3,4,5)
print(a)

fruits = ("Mango", "Apple", "Banana", "cherry")
print(fruits)
print(type(fruits))
fruitsList = list(fruits)
fruitsList[1] = "pineapple"
print(fruitsList)
print(type(fruitsList))
fruitTuple = type(fruitsList)
#fruitTuple[2] ="Carrot" -- not possible
print(type(fruitTuple))
print(fruitsList)
print(fruitsList[1:])

fruit = ("berry",)

fruitConcat = fruits + fruit

print(fruitConcat)

a = (1,2,3,4,5,6,8,10)
x= a.count(5) # returns no.of occurences
print(x)

print(a.index(3)) # index of element 3. shows the index value of the first occurence

fruitsSet = {"Mango", "Apple", "Banana", "Cherry", "Mango"}
print(fruitsSet)

fruitSettoList = list(fruitsSet)
print(fruitSettoList)
fruitSettoList.append("Mango")
print(fruitSettoList)
fruity = set(fruitSettoList) #set - no duplicates allowed, unordered
print(fruity)

fruitt = {"Dragonfruit",}
fruitt.update("mango")
print(fruitt)
fruitt.remove("Dragonfruit")
print(fruitt)


#update and union can be used to add 2 sets
a= {1,2,3,4,5,6,7}
b={1,5,7,9,8}

print(a.union(b))


my_dict = {
    "name" : "Shally",
    "age" : 30,
}

print(my_dict)

a = {
    "name" : ["Shally", "Shreya", "Vishnu"],
    "age" : 21,
    "year " : 1999,
}

print(a)

a = dict(name = "Tanmay", age = 27, country = "India")
print(a)
print(a["name"])
print(a.keys())
print(a.values())