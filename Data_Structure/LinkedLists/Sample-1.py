class SinglyNode: # creating blueprint
    def __init__(self, data, next=None): # _init_ is a constructor, self is an instance of the node
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

Head = SinglyNode(5)
node1 = SinglyNode(10)
node2 = SinglyNode(20)
node3 = SinglyNode(30)

Head.next = node1
node1.next = node2
node2.next = node3

# Traversing
curr = Head

while curr:
    print(curr)
    curr = curr.next

# Searching
data = 20

while curr is not None:
    if curr.data == data:
        print('Found!')
        break

    curr = curr.next  