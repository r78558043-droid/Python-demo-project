

def greet(name):
    print(f"Hello, {name}!")          # Function and string formatting

def square_numbers(nums):
    for n in nums:                    # Loop through list
        print(f"{n} squared is {n**2}")

greet("Revathi")                      # Function call
x = 12                                # Variable assignment
if x % 2 == 0:                        # Condition check
    print(x, "is even")
else:
    print(x, "is odd")

fruits = ["apple", "banana", "cherry"]  # List example
square_numbers([1, 2, 3, 4])            # Call function with list
print("Reversed word:", "Python"[::-1]) # String slicing
