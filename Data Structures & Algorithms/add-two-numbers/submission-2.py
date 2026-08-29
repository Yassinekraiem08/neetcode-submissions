# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy 
        curr1 = l1
        curr2 = l2
        carry = 0

        while curr1 or curr2 or carry:
            if curr1 == None:
                val1 = 0
            else:
                val1 = curr1.val

            if curr2 == None:
                val2 = 0
            else:
                val2 = curr2.val 

            current_sum = val1 + val2 + carry
            
            digit = current_sum  % 10
            carry = current_sum // 10

            if curr1:
                curr1 = curr1.next
            if curr2: 
                curr2 = curr2.next
                
            tail.next = ListNode(digit)
            tail = tail.next
        
        return dummy.next