# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        carry = 0
        curr1 = l1
        curr2 = l2

        while curr1 and curr2:
            total = curr1.val + curr2.val + carry
            digit = total % 10
            carry = total // 10
            tail.next = ListNode(digit)

            tail = tail.next
            curr1 = curr1.next
            curr2 = curr2.next
        
        while curr1:
            total = curr1.val + carry
            digit = total % 10
            carry = total // 10

            tail.next = ListNode(digit)
            tail = tail.next
            curr1 = curr1.next
        
        while curr2:
            total = curr2.val + carry
            digit = total % 10
            carry = total // 10

            tail.next = ListNode(digit)
            tail = tail.next
            curr2 = curr2.next
        
        if carry:
            tail.next = ListNode(carry)

        return dummy.next