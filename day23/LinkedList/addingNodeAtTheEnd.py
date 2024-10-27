from implementation import Node
from print import printLinkedList

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1
current = head
printLinkedList(current)

new_node = Node(50)

while current.next is not None:
    current = current.next
current.next = new_node

printLinkedList(head)