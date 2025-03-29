class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    pushed_node = Node(data)
    pushed_node.next = head
    return pushed_node

def build_one_two_three():
    _root = Node(1)
    _cur = _root
    for i in range(2, 4):
        _cur.next = Node(i)
        _cur = _cur.next
    return _root
