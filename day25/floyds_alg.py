class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def cycle_detection(head):
    turtle = head
    rabbit = head
    
    while turtle is not None and rabbit is not None and rabbit.next is not None:
        turtle = turtle.next
        rabbit = rabbit.next.next
        if rabbit == turtle:
            return True
    return False

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3

print(cycle_detection(node1))
