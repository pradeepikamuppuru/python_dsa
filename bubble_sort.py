# Read input values
n = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))

# Get the length of the list
length = len(arr)

# Bubble sort algorithm
for i in range(length - 1):
    # Flag to detect any swap
    swapped = False
    # Last i elements are already in place
    for j in range(length - 1 - i):
        # Swap if the element found is greater than the next element
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
    # If no two elements were swapped in the inner loop, break
    if not swapped:
        break

# Print the sorted list
print("Sorted list:", arr)
