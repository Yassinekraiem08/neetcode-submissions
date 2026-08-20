# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        values = []

        for nodes in lists:
            while nodes:
                values.append(nodes.val)
                nodes = nodes.next
        
        values.sort()
        
        for value in values:
            tail.next = ListNode(value)
            tail = tail.next

        return dummy.next