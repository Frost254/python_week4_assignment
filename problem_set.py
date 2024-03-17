large_power = lambda num,power: True if pow(num,power) >= 5000 else False

power = int(input("Enter the exponent: "))
number = int(input("Enter the number: "))

print(large_power(number, power))

divisible_by_10 = lambda num: True if num % 10 == 0 else False
print(divisible_by_10(number))
