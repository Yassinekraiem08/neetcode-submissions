# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr2 = slow
        prev = None
        while curr2:
            next_temp = curr2.next
            curr2.next = prev
            prev = curr2
            curr2 = next_temp

        curr1 = head
        curr2 = prev
        twin_sum = 0

        while curr1 and curr2:
            current_sum = curr1.val + curr2.val
            curr1 = curr1.next
            curr2 = curr2.next

            twin_sum = max(twin_sum, current_sum)
        
        return twin_sum
