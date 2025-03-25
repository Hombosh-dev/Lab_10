def stringify(node):
    _str = ""
    
    while node != None:
        _str += f"{node.data} -> "
        node = node.next
    
    _str += "None"
    return _str