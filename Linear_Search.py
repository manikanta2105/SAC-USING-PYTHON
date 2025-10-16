def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index  
    return -1  


numbers = list(map(int, input("Enter the numbers (space-separated):\n").split()))

target_value = int(input("Enter the number to search:\n"))


result = linear_search(numbers, target_value)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
