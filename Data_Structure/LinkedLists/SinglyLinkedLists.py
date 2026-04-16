# Singly Linked Lists

# Blueprint
class SinglyNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next    

# Node creation
head = SinglyNode(10)
A = SinglyNode(20)
B = SinglyNode(30)
C = SinglyNode(40)

head.next = A
A.next = B
B.next = C

# My Traversing
def traversing(curr):
    arr = []

    while curr:
        arr.append(curr.data)
        curr = curr.next

    return arr

# AI Traversing:

# def traversing(curr):
#     result = ""

#     while curr:
#         result += str(curr.data) + " → "
#         curr = curr.next

#     result += "None"
#     return result

# My Inserting At Beginning

def insert_at_beginning(val):
    new_node = SinglyNode(val)
    new_node.next = head
    return new_node


print_new_head = insert_at_beginning(2)
printVal = traversing(print_new_head)
print(printVal)

    


