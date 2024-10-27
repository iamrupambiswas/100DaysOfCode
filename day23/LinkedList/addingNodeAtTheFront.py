from implementation import Node
from print import printLinkedList

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

current = node1
printLinkedList(current)

new_node = Node(50)
new_node.next = current
current = new_node
printLinkedList(current)
