class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    current = head
    head = None
    while current is not None:
        new_node = Node(current.data)
        new_node.next = head
        head = new_node
        current = current.next
    return head
