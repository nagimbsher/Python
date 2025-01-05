my_matrix = '''

    7ii
    Tsx
    h%?
    i #
    sM
    $a
    #t%
    ^r!

'''

# Convert the matrix into a list of lists, ignoring empty rows
final_matrix = [list(row) for row in my_matrix.split('\n') if row.strip()]
print(final_matrix)

# Initialize the final result
final_result = ""

# Determine the maximum number of columns in the matrix
max_cols = max(len(row) for row in final_matrix)

# Iterate column by column
for col_index in range(max_cols):
    for row_index in range(len(final_matrix)):
        # Safely access each cell, skipping if the column index is out of range
        if col_index < len(final_matrix[row_index]):
            char = final_matrix[row_index][col_index]
            if char.isalpha():
                final_result += char
            elif final_result != "" and final_result[-1] != " ":
                final_result += " "

# Print the final result
print(final_result.strip())  # Strip trailing spaces

# Example of importing and using math
import math
print("Value of e:", math.e)
