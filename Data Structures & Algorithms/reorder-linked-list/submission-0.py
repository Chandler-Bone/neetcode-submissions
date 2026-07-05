# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow_node = head
        fast_node = head

        while fast_node and fast_node.next:
            if not fast_node.next.next:
                fast_node = fast_node.next
            else:
                fast_node = fast_node.next.next
                slow_node = slow_node.next

        second = slow_node.next
        slow_node.next = None
        prev_node = None

        while second:
            temp_node = second.next
            second.next = prev_node
            prev_node = second
            second = temp_node
            
        first = head
        second = prev_node

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
