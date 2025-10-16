def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


num = int(input("Enter the position to find the Fibonacci number: "))

if num < 0:
    print("Please enter a non-negative integer.")
else:
    result = fibonacci(num)
    print(f"Fibonacci number at position {num} is {result}")
