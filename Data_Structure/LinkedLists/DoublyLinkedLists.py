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
    

print(traversingBackward(B))
