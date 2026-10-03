 # Find duplicate elements in an array

# Take array input from the user
arr = [int(x) for x in input(
    "Enter array elements separated by space: "
).split()]

# Find duplicate elements
duplicates = []

for element in arr:
    if arr.count(element) > 1 and element not in duplicates:
        duplicates.append(element)

# Display the result
if duplicates:
    print("Duplicate elements are:", duplicates)
else:
    print("No duplicate elements found.")