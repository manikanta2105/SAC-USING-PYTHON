#Create a list
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

#Access elements
print("First item:", fruits[0])
print("Last item:", fruits[-1])

#Add elements
fruits.append("orange")         
print("After append:", fruits)

fruits.insert(1, "mango")       
print("After insert:", fruits)

#Remove elements
fruits.remove("banana")         
print("After remove banana:", fruits)
#remove last item
popped_item = fruits.pop()
print("Popped item:", popped_item)
print("After pop:", fruits)
# remove first item
popped_first = fruits.pop(0)     
print("Popped first item:", popped_first)
print("After popping first:", fruits)

#Check if element exists
if "cherry" in fruits:
    print("Cherry is in the list")

#Loop through list
print("Looping through list:")
for fruit in fruits:
    print(fruit)

# Length of list
print("Length of list:", len(fruits))

#Slice list
print("Slice fruits[0:2]:", fruits[0:2])

#Combine lists
veggies = ["carrot", "lettuce"]
all_food = fruits + veggies
print("Combined list:", all_food)

#Sort list
numbers = [4, 2, 8, 1, 5]
numbers.sort()
print("Sorted numbers:", numbers)
numbers.sort(reverse=True)
print("Reverse sorted numbers:", numbers)
