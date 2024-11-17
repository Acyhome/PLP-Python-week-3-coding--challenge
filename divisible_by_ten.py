def divisible_by_ten(num):
    # Step 1: Use the modulus operator (%) to find the remainder
    if num % 10 == 0:
        return True  # Return True if the number is divisible by 10
    else:
        return False  # Return False if the number is not divisible by 10

# Example usage of the function
num = 20
print(divisible_by_ten(num))  # Output: True because 20 is divisible by 10

num = 15
print(divisible_by_ten(num))  # Output: False because 15 is not divisible by 10
