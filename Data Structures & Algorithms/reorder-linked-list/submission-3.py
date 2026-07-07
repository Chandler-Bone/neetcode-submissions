# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head.next:
            return

        fast = head
        slow = head

        while fast and fast.next:
            if fast.next.next:
                slow = slow.next
                fast = fast.next.next
            else:
                fast = fast.next

        second = slow.next
        slow.next = None
        prev_node = None

        while second:
            temp = second.next
            second.next = prev_node
            prev_node = second
            second = temp

        end_node = prev_node
        node = head

        while node and end_node:
            temp_node = node.next
            node.next = end_node
            node = temp_node

            temp_node = end_node.next
            end_node.next = node
            end_node = temp_node
            
