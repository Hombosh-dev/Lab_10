def loop_size(node):
    slow = node
    fast = node
    count = 0

    while fast:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = slow.next
            while fast != slow:
                slow = slow.next
                count += 1
            return count + 1
    return count
