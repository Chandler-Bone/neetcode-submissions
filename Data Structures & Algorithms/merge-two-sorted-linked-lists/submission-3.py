# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        node = ListNode()
        dummy = node
        list1_node = list1
        list2_node = list2

        while list1_node and list2_node:
            
            if list1_node.val <= list2_node.val:
                node.next = list1_node
                list1_node = list1_node.next
                node = node.next
            else:
                node.next = list2_node
                list2_node = list2_node.next
                node = node.next
        
        if list1_node:
            node.next = list1_node
        
        if list2_node:
            node.next = list2_node

        return dummy.next

        