class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(s):
    _elements = s.split(' -> ')[:-1]
    _root = None

    for i in range(len(_elements) - 1, -1, -1):
        _root = Node(int(_elements[i]), _root)
    return _root
