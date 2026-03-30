class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)
    
Head = DoublyNode(5)
A = DoublyNode(10)
B = DoublyNode(20)
C = DoublyNode(30)
D = DoublyNode(40)

Head.next = A
A.next = B
A.prev = Head
B.next = C
B.prev = A
C.next = D
C.prev = B
D.prev = C

# Display
def display(Head):
    curr = Head
    element = []

    while curr:
        element.append(str(curr.val))
        curr = curr.next

    print(' <-> '.join(element))

# Insterting at the beginning
def insert_at_beginning(val):
    new_node = DoublyNode(val, next=Head, prev=None)
    Head.prev = new_node