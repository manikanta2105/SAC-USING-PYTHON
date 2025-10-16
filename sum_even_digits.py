def sum_even_digits(number):
    total = 0
    for digit in str(number):
        if int(digit) % 2 == 0:
            total += int(digit)
    return total

num = int(input("Enter a number: "))                                
result = sum_even_digits(num)
print("Sum of even digits:", result)
