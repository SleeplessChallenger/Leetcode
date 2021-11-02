# 1. Linked List Cycle II
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return None
        
        slow = head.next
        fast = head.next.next
        
        while slow != fast:
            if fast is None or fast.next is None:
                return None
            
            slow = slow.next
            fast = fast.next.next
        
        curr = head
        
        while curr != slow:
            curr = curr.next
            slow = slow.next
        
        return curr

# 2. Intersection of Two Linked Lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # O(n) Space
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        hashset = set()
        
        curr = headA
        while curr:
            hashset.add(curr)
            curr = curr.next
        
        curr = headB
        while curr:
            if curr in hashset:
                return curr
            
            curr = curr.next
        
        return None
    
    # O(1) Space
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        sizeA = self.count(headA)
        sizeB = self.count(headB)
        
        if sizeA > sizeB:
            diff = sizeA - sizeB
            return self.get_result(diff, headA, headB)
        else:
            diff = sizeB - sizeA
            return self.get_result(diff, headB, headA)
        
    def get_result(self, diff, long_node, short_node):     
        while diff:
            diff -= 1
            long_node = long_node.next
        
        while long_node != short_node:
            if long_node is None or short_node is None:
                return None
            
            long_node = long_node.next
            short_node = short_node.next
        
        return long_node
        
        
    def count(self, node):
        count = 0
        while node:
            count += 1
            node = node.next
        
        return count
