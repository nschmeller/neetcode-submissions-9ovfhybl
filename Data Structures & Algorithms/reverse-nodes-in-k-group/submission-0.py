# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sentinel = group_prev = ListNode(next=head)
        while True:
            end = group_prev
            for _ in range(k):
                end = end.next
                if not end:
                    return sentinel.next

            group_next = end.next
            prev, curr = group_next, group_prev.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev, curr = curr, temp

            old_head = group_prev.next
            group_prev.next = end
            group_prev = old_head
