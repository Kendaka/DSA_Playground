class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# creating nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# linking those nodes
node1.next = node2
node2.next = node3

# assignment of head
head = node1

# example
current = head
target_index = 3 
for i in range(target_index):
    current = current.next
print(current.value) 