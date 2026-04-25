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
    new_node.next = head
    if head == None:
        return new_node
    head.prev = new_node
    return new_node

head = insert_at_beginning(head, 4)
print(traversingForward(head))