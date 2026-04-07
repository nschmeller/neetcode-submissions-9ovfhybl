# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappush, heappop
from itertools import count

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap, counter = [], count()
        for head in lists:
            heappush(heap, (head.val, next(counter), head))
        
        sentinel = curr = ListNode()
        while curr and heap:
            _, _, node = heappop(heap)
            curr.next = node
            if node.next:
                heappush(heap, (node.next.val, next(counter), node.next))
            curr = curr.next
        
        return sentinel.next
