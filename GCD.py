def GCD(l, s):
    r = l % s
    if r == 0:
        return s
    else:
        return GCD(s, r)

number = int(input("Enter the first number: "))
while number <= 0:
    print("Please enter a positive integer.")
    number = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
while number2 <= 0:
    print("Please enter a positive integer.")
    number2 = int(input("Enter the second number: "))
result = GCD(max(number, number2), min(number, number2))
print(f"The GCD of {number} and {number2} is {result}.")