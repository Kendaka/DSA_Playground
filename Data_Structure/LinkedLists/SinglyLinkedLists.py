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
D = SinglyNode(40)

A.next = B
B.next = C
C.next = D

# Traversing
def traversing(curr):
    result = ""

    while curr:
        result += str(curr.data) + " → "
        curr = curr.next

    result += "None"
    return result

printVal = traversing(A)
print(printVal)

# Inserting

