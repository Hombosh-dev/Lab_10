class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    if source is None:
        raise ValueError()
    push_dest = Node(source.data)
    source = source.next
    push_dest.next = dest
    return Context(source, push_dest)