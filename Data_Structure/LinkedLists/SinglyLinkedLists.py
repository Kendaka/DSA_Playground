# Singly Linked Lists

# Blueprint
class SinglyNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next    

# Node creation
head = SinglyNode(10)
B = SinglyNode(20)
C = SinglyNode(30)
D = SinglyNode(40)

A.next = B
B.next = C
C.next = D

# My Traversing
def traversing(curr):
    arr = []

    while curr:
        arr.append(curr.data)
        curr = curr.next

    return arr

printVal = traversing(A)

# AI Traversing:

# def traversing(curr):
#     result = ""

#     while curr:
#         result += str(curr.data) + " → "
#         curr = curr.next

#     result += "None"
#     return result

# Inserting
def insert_at_beginning(curr):
    curr.next = head
    head = curr
    return curr
    


