class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse(head):
    prev = None
    current = head

    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt

    return prev


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

new_head = reverse(head)

while new_head:
    print(new_head.data, end=" ")
    new_head = new_head.next
