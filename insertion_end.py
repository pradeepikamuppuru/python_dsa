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


def insertion_end(Head, val):
    if Head is None:
        return Node(val)
    current = Head
    while current.next:
        current = current.next
    current.next = Node(val)
    return Head

arr = [2,3,45,1,6]
res = array_to_ll(arr)
res1 = insertion_end(res, 7)
print_ll(res1)
