class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    new_node = Node(data)
    
    if head is None or data < head.data:
        new_node.next = head
        return new_node

    _cur = head
    while _cur.next and _cur.next.data < data:
        _cur = _cur.next
    
    new_node.next = _cur.next
    _cur.next = new_node
    
    return head 