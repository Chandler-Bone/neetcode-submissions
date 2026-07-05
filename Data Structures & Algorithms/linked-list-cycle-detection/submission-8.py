# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        fast_node = head
        slow_node = head

        while fast_node and fast_node.next:
            
            fast_node = fast_node.next.next
            slow_node = slow_node.next

            if fast_node == slow_node:
                return True

        return False