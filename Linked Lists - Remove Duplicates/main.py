class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None:
        return

    curr = head
    new_head = Node(curr.data)
    tail = new_head
    value_set = set({curr.data})
    
    while curr.next is not None:
        curr = curr.next
        if curr.data in value_set:
            continue
        value_set.add(curr.data)
        new_node = Node(curr.data)
        tail.next = new_node
        tail = new_node
    return new_head
