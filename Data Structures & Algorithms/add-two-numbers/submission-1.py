# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode()

        curr, curr1, curr2 = sentinel, l1, l2
        carry = 0
        while curr1 and curr2:
            curr_sum = curr1.val + curr2.val + carry
            digit, carry = curr_sum % 10, curr_sum // 10
            curr.next = ListNode(val=digit)
            curr, curr1, curr2 = curr.next, curr1.next, curr2.next
        
        while curr1:
            curr_sum = curr1.val + carry
            digit, carry = curr_sum % 10, curr_sum // 10
            curr.next = ListNode(val=digit)
            curr, curr1 = curr.next, curr1.next
        
        while curr2:
            curr_sum = curr2.val + carry
            digit, carry = curr_sum % 10, curr_sum // 10
            curr.next = ListNode(val=digit)
            curr, curr2 = curr.next, curr2.next
        
        if carry > 0:
            curr.next = ListNode(val=carry)
        
        return sentinel.next
