class DoublyNode:
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)
    
Head = 0
A = 10
B = 20
C = 30
D = 40

Head.next = A
A.next = B
A.prev = Head
B.next = C
B.prev = A
C.next = D
C.prev = B
D.prev = C
    
