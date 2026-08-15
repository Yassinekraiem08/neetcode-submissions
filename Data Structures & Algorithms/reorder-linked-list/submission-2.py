# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr2 = slow.next
        slow.next = None

        prev = None
        
        while curr2:
            next_temp = curr2.next
            curr2.next = prev
            prev = curr2
            curr2 = next_temp

        curr2 = prev
        curr1 = head

        while curr1 and curr2:
            next_temp1 = curr1.next
            next_temp2 = curr2.next

            curr1.next = curr2
            curr2.next = next_temp1


            curr1 = next_temp1
            curr2 = next_temp2

        return None