# ============================================================
#              FIND SECOND LARGEST ELEMENT
# ============================================================


# ------------------------------------------------------------
# Driver Code
# ------------------------------------------------------------

# Take array elements from the user
arr = [
    int(x)
    for x in input("Enter array elements separated by space: ").split()
]


# ------------------------------------------------------------
# Check whether the array contains at least two elements
# ------------------------------------------------------------

if len(arr) < 2:
    print("Please enter at least two elements.")

else:
    # Sort the array in ascending order
    arr.sort()

    # The second largest element is at index -2
    second_largest = arr[-2]

    # Display the result
    print("Second largest element is:", second_largest)
