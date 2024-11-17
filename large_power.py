def large_power(base, exponent):
    # Step 1: Calculate base raised to the power of exponent
    result = base ** exponent
    
    # Step 2: Check if the result is greater than 5000
    if result > 5000:
        return True  # If the result is greater than 5000, return True
    else:
        return False  # Otherwise, return False

# Example usage of the function
base = 5
exponent = 5
print(large_power(base, exponent))  # Output: False, because 5^5 = 3125 (less than 5000)
