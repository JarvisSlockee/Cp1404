"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    When an input that is not a number is entered
2. When will a ZeroDivisionError occur?
    When you enter 0 as the denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    No
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
