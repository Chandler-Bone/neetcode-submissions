# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        curr = head
        count = 0

        start = head
        left_node = head
        left_prev = None
        right_node = None
        tail = None

        while curr:
            count += 1
            next_node = curr.next
            if count % k == 0:
                right_node = curr
                right_node.next = None
                
                rev_head, rev_tail = self.reverse(left_node)
                if left_prev:
                    left_prev.next = rev_head
                left_prev = left_node
                start = rev_head if start == head else start
                
                rev_tail.next = next_node
                left_node = next_node
            
            
            curr = next_node

        return start



    def reverse(self, head):
        prev = None
        tail = curr = head
        while curr:
            # print(curr.val)
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        head = prev
        return head, tail
            

            

