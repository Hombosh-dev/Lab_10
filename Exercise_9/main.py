class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def swap_pairs(head):
    if not head or not head.next:
        return head

    pointer_head = Node(None)
    pointer_head.next = head
    prev = pointer_head

    while head and head.next:
        first = head
        second = head.next
        prev.next = second
        first.next = second.next
        second.next = first

        prev = first
        head = first.next
    head = pointer_head.next
    return head

node_1 = Node('A')
node_2 = Node('B')
node_3 = Node('C')
node_2.next = node_3
node_1.next = node_2

swap_pairs(node_1)
