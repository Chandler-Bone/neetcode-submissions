# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        curr_res = res

        curr_l1 = l1
        curr_l2 = l2
        carry = 0

        while curr_l1 or curr_l2 or carry:
            curr_res.next = ListNode()
            curr_res = curr_res.next
            total = 0
            total += curr_l1.val if curr_l1 else 0
            total += curr_l2.val if curr_l2 else 0
            total += carry

            carry = total // 10
            total = total % 10
            curr_res.val = total

            curr_l1 = curr_l1.next if curr_l1 else None
            curr_l2 = curr_l2.next if curr_l2 else None

        return res.next
