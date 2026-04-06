# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappush, heappop

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sentinel = curr = ListNode()
        heap = []

        for idx, l in enumerate(lists):
            heappush(heap, (l.val, idx, l))
        
        while heap:
            val, idx, node = heappop(heap)
            curr.next = ListNode(val=val)
            curr = curr.next
            if node.next:
                heappush(heap, (node.next.val, idx, node.next))
        
        return sentinel.next
