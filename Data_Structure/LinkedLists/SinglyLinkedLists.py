# Singly Linked Lists

# Blueprint
class SinglyNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next    

# Node creation
A = SinglyNode(10)
B = SinglyNode(20)
C = SinglyNode(30)

A.next = B
B.next = C

curr = A

while curr:
    arr = []
    arr.append[curr.data]
