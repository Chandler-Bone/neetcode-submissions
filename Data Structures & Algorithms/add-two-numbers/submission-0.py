# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        node1 = l1
        node2 = l2

        curr_node = ListNode()
        start = curr_node 

        carry = 0

        while node1 or node2 or carry > 0:
            new_node = ListNode()
            curr_node.next = new_node
            curr_node = curr_node.next

            node_sum = 0
            node_sum += node1.val if node1 else 0
            node_sum += node2.val if node2 else 0
            node_sum += carry

            curr_node.val = node_sum % 10
            carry = node_sum // 10

            node1 = node1.next if node1 else None
            node2 = node2.next if node2 else None

        return start.next