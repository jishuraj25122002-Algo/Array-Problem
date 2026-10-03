# Remove duplicates while preserving order

arr = [int(x) for x in input(
    "Enter array elements separated by space: "
).split()]

unique_elements = list(dict.fromkeys(arr))

print("Array after removing duplicates:", unique_elements)