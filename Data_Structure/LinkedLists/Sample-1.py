class SinglyNode: # creating blueprint
    def __init__(self, data, next=None): # _init_ is a constructor, self is an instance of the node
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

Head = SinglyNode(10)
node1 = SinglyNode(20)
node2 = SinglyNode(20)
