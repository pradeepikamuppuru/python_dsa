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

def deletion_kth(Head, k):
    if (Head == None):
        return Head
    if (k == 1):
        temp = Head
        Head = Head.next
        return Head
    temp = Head
    count = 1
    prev = None
    while(temp!= None):
        if(count == k):
            if prev:
                prev.next = temp.next
            else:
                Head = temp.next
            break
        prev = temp
        temp = temp.next
        count += 1
    return Head


arr = [2,3,4,1,5,3]
result = array_to_ll(arr)
result = deletion_kth(result, 3)
print_ll(result)
