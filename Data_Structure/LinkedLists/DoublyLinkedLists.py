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
    if head is None:
        return DoublyNode(value)

    curr = head

    while curr:
        if curr.data == target_val:
            new_node = DoublyNode(value)

            temp = curr.next  # store right side node

            # link left → new
            curr.next = new_node
            new_node.prev = curr

            # link new → right
            new_node.next = temp

            # fix right side back-link (ONLY if it exists)
            if temp:
                temp.prev = new_node

            return head

        curr = curr.next

    return head 

# Deletion
def delete_node(head, target_val):  
    if head is None:
        return None

    curr = head

    while curr:
        if curr.data == target_val:

            if curr.prev is None:
                head = curr.next
                if head: 
                    head.prev = None
                return head

            if curr.next: # adjusted by perv.s
                curr.next.prev = curr.prev

            curr.prev.next = curr.next

            return head

        curr = curr.next

    return head
