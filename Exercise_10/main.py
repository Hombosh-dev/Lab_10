class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError()
    first = Node(head.data)
    second = Node(head.next.data)
    first_curr = first
    second_curr = second

    head = head.next.next
    toggle = True
    while head:
        if toggle:
            first_curr.next = Node(head.data)
            first_curr = first_curr.next
        else:
            second_curr.next = Node(head.data)
            second_curr = second_curr.next
        toggle = not toggle
        head = head.next
    return Context(first, second)
