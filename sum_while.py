n = int(input("Enter a number: "))
s = 0
while n:
    s += n % 10
    n //= 10
print("Sum of digits:", s)
