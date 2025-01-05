def calculation(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction  # Return both values as a tuple

# Call the function and capture the returned values
res = calculation(40, 10)

# Access the results using indexing
print(res[0])  # Prints the addition result
print(res[1])  # Prints the subtraction result
