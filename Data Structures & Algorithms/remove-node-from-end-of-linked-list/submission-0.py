# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sentinel = ListNode(next=head)
        left, right = sentinel, head

        remaining = n
        while remaining > 0:
            right = right.next
            remaining -= 1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next

        return sentinel.next
