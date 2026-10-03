 # Find the missing number in an array

# Take array input from the user
arr = [int(x) for x in input(
    "Enter array elements separated by space: "
).split()]

# Total number of elements should be from 1 to n
n = len(arr) + 1

# Calculate the expected sum from 1 to n
expected_sum = n * (n + 1) // 2

# Calculate the actual sum of array elements
actual_sum = sum(arr)

# Find the missing number
missing_number = expected_sum - actual_sum

# Display the result
print("Missing number is:", missing_number)