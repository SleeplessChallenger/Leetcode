# 1. Add Two Numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        1. Start from leftmost number and use carry
            if it reaches 10+
        2. Apply carry to the next number
        
        Process:
        1. sum to digits
        2. apply % 10 to get without carry
        3. create LinkedList and move node
        4. get the carry
        5. move to the next node of both lists
        
        Crucial: also factor in the case when
            only one list is still valid as the
            length can be not-equal
            + we need to continue if there is
            left carry
        '''
        
        head = ListNode(0)
        total = head
        carry = 0
        
        while l1 or l2 or carry != 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            
            lists_sum = l1_val + l2_val + carry
            no_carry = lists_sum % 10
            
            node = ListNode(no_carry)
            total.next = node
            total = node
            
            carry = lists_sum // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return head.next
