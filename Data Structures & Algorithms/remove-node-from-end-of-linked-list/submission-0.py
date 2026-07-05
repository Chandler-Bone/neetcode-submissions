# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0
        node = head
        
        while node:
            length += 1
            node = node.next

        target_idx = length - (n - 1)
        print(target_idx)

        prev_node = None
        post_node = None
        cur_idx = 0
        node = head
        while node:
            cur_idx += 1
            if cur_idx == target_idx - 1:
                prev_node = node 
            if cur_idx == target_idx + 1:
                post_node = node 
            print(cur_idx)
            print(prev_node)
            print(post_node)

            node = node.next
        
        if prev_node:
            prev_node.next = post_node
        else:
            head = post_node
        
        return head
        