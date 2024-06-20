class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def array_to_ll(array):
    if not array:
        return None
    
    # Initialize the head node with the first element
    Head = Node(array[0])
    current = Head
    
    # Loop through the rest of the elements
    for value in array[1:]:
        current.next = Node(value)
        current = current.next
    
    return Head

def print_ll(Head):
    current = Head
    while current:
        print(current.value, end="->")
        current = current.next
    print("None")

# Example usage
arr = [2, 4, 1, 5, 3]
result = array_to_ll(arr)
print_ll(result)  # Should print: 2->4->1->5->3->None
