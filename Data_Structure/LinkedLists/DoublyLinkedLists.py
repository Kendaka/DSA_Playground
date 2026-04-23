# Doubly Linked Lists

# Doubly Node

class DoublyNode:
    def __init__(self, data, prev, next=None):
        self.data = data
        self.prev = prev
        self.next = next
# Creating Nodes 
head = (5)
A = (10)
B = (15)
C = (20)
D = (25)

# Connecting Next Pointers
head.next = A
A.next = B
B.next = C