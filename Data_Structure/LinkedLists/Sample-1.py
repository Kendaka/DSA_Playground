
class SinglyNode: # creating blueprint
    def __init__(self, data, next=None): # _init_ is a constructor, 
        self.data = data
        self.next = next

node = SinglyNode(10)
print(node)
