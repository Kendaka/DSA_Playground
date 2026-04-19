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


# AI Beginning Insertion
# def insert_at_beginning(head, val):
#     new_node = SinglyNode(val)
#     new_node.next = head
#     return new_node

# head = insert_at_beginning(head, 2)
# print(traversing(head))


# Insertion
def insert_after(head, target_value, value):
    curr = head

    while curr:
        if curr.data == target_value:
            new_node = SinglyNode(value)
            new_node.next = curr.next
            curr.next = new_node
            return head 
        curr = curr.next

    return head

head = insert_after(head, 30, 23)
    
# End Instertion
def insert_last(head, value):
    curr = head

    while curr.next is not None:
        curr = curr.next

        if head == None:
            return head

    new_node = SinglyNode(value)    
    curr.next = new_node

    return head

insert_last(head, 77)
print(traversing(head))
# Searching
