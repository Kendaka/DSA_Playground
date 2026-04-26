# Doubly Linked Lists

# Doubly Node

class DoublyNode:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.prev = prev
        self.next = next

# Creating Nodes 
head = DoublyNode(5)
A = DoublyNode(10)
B = DoublyNode(15)
C = DoublyNode(20)
D = DoublyNode(25)

# Connecting Next Pointers
head.next = A
A.next = B
B.next = C
C.next = D

# Connecting Tail Pointers
A.prev = head
B.prev = A
C.prev = B
D.prev = C

# Traversal
def traversingForward(curr):
    result = ""

    while curr:
        result += str(curr.data) + "->"
        curr = curr.next

    result += "None"
    return result

def traversingBackward(curr):
    result = ""
    
    while curr:
        result += str(curr.data) + "->"
        curr = curr.prev

    result += "None"
    return result
    

# Beginning Insertion
def insert_at_beginning(head, val):
    new_node = DoublyNode(val)

    # 1. empty list
    if head is None:
        return new_node

    # 2. go to tail
    curr = head
    while curr.next:
        curr = curr.next

    # 3. connect
    curr.next = new_node
    new_node.prev = curr

    return head


# Middle Insertion
def insert_after(head, target_val, value):
    new_node = DoublyNode(value)
    curr = head

    if head is None:
        return new_node

    while curr:
        if curr.data == target_val:

            new_node.next = curr.next
            curr.next = new_node
            new_node.prev = curr
            return head
        
        curr = curr.next
    return head

            