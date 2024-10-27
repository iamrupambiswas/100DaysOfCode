def printLinkedList(head):
    while head is not None:
        print(head.data, end="->")
        head = head.next
    print("None")