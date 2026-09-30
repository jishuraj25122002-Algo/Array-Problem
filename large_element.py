 # Function to find the largest element in an array
def find_largest(arr):
    largest = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]

    return largest


# Driver Code
arr = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

# Function call
largest = find_largest(arr)

print("Array:", arr)
print("Largest element:", largest)