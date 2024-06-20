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

def print_ll(Head):
    current = Head
    while current:
        print(current.value, end="->")
        current = current.next
    print("None")



def delete_head(Head):
    if not Head:
        return None
    return Head.next


arr = [2,4,1,5,3]
result = array_to_ll(arr)
deletion_head = delete_head(result)
print_ll(deletion_head)


