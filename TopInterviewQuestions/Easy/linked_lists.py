# 1. Delete Node in a LinkedList
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next is None:
            node = None
        else:
            node.val = node.next.val
            node.next = node.next.next

# 2. Palindrome Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # stack. Time: O(n) Space: O(n)
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = self.createStack(head)
        while len(stack) != 0:
            node = stack.pop()
            if node.val != head.val:
                return False
            head = head.next
        
        return True
        
    def createStack(self, curr):
        arr = []
        while curr:
            arr.append(curr)
            curr = curr.next
        
        return arr
    
    # using 2 pointers & reverse
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        newHead = self.getHead(head)
        while newHead:
            if newHead.val != head.val:
                return False
            newHead = newHead.next
            head = head.next
        
        return True
        
    def getHead(self, curr):
        fast = curr
        slow = curr
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return self.reverseHead(slow)
    
    def reverseHead(self, head):
        prev, nx = None, None
        curr = head
        while curr:
            nx = curr.next
            curr.next = prev
            prev = curr
            curr = nx
        
        return prev
