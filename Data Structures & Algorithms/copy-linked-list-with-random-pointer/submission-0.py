"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        sentinel = Node(0)
        old, new, nodes = head, sentinel, {}
        while old:
            new.next = Node(old.val)
            nodes[old] = new.next
            old, new = old.next, new.next
        
        old, new = head, sentinel.next
        while old and new:
            if old.random:
                new.random = nodes[old.random]
            old, new = old.next, new.next
        
        return sentinel.next
