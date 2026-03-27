class SinglyNode: # creating blueprint
    def __init__(self, data, next=None): # _init_ is a constructor, self is an instance of the node
        self.data = data
        self.next = next

node1 = SinglyNode(10)
node2 = SinglyNode(20)
print(node1.data)
