class Node:
    def __init__(self, value1, next1 = None):
        self.value = value1
        self.next = next1

def array_to_ll(array):
    if not array:
        return None
    Head = Node(array[0])
    current = Head
    for value in array[1:]:
        current.next = Node(value)
        current = current.next
    return Head
)

def count_length(Head):
    current = Head
    count = 0
    while current:
        count +=1
        current = current.next
    return count



arr = [2,4,1,5,3]
result = array_to_ll(arr)
length = count_length(result)
print(length)

