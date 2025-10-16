def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            left = mid + 1  
        else:
            right = mid - 1  

    return -1 


numbers = list(map(int, input("Enter the numbers (space-separated):\n").split()))


target_value = int(input("Enter the number to search:\n"))

result = binary_search(numbers, target_value)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
