# Read input values
n = int(input("Enter the number of elements: "))
unsorted = list(map(int, input("Enter the elements: ").split()))

# Get the length of the list
length = len(unsorted)

# Selection sort algorithm
for i in range(length - 1):
    # Assume the minimum element is the first element
    mini = i
    
    # Find the minimum element in the remaining unsorted array
    for j in range(i + 1, length):
        if unsorted[j] < unsorted[mini]:
            mini = j
    
    # Swap the found minimum element with the first element
    unsorted[i], unsorted[mini] = unsorted[mini], unsorted[i]

# Print the sorted list
print("Sorted list:", unsorted)
