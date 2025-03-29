class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def get_nth(node, index):
    if index < 0 or node == None:
        raise ValueError()
    _data = None
    for _ in range(index):
        node = node.next
        if node == None:
            raise ValueError()
    return node