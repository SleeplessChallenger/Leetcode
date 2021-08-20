# 1. easy - Reverse Linked List
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        nx = None
        curr = head
        
        while curr:
            nx = curr.next
            curr.next = prev
            prev = curr
            curr = nx
        
        return prev

# 2. easy - Linked List Cycle
class Solution:
    
    # brute force
    def hasCycle(self, head: ListNode) -> bool:
        ht = {}
        curr = head
        while curr:
            if curr in ht:
                return True
            
            ht[curr] = True
            curr = curr.next
        return False
    
    # more optimal
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return  False
        fast = head.next
        slow = head
        while fast != slow:
            if fast is None or fast.next is None:
                return False
    
            slow = slow.next
            fast = fast.next.next
        
        return True

# 3. easy - Merge Two Sorted Lists

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None or l2 is None:
            return l1 if l2 is None else l2
        
        head1 = l1
        head2 = l2
        prev = None
        while head1 and head2:
            if head1.val < head2.val:
                prev = head1
                head1 = head1.next
            else:
                if prev is not None:
                    prev.next = head2
                prev = head2
                head2 = head2.next
                prev.next = head1
        
        if head1 is None:
            prev.next = head2
        
        return l1 if l1.val < l2.val else l2
        
        
