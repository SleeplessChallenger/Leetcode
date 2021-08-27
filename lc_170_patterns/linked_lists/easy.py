# 1. Middle of the Linked List
class Solution:
    # if odd: after loop we're done
    # elif even: after loop we need to
    # do one more step.
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        slow = head
        fast = head.next
        
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        
        return slow if fast is None else slow.next
# PS: another way is to start with both pointers at head

# 2. Remove Duplicates from Sorted List
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        curr = head
        while curr:
            nx = curr.next
            while nx and curr.val == nx.val:
                nx = nx.next
            
            curr.next = nx
            curr = curr.next
        
        return head

# 3. Remove Linked List Elements
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        curr = head
        
        tempHead = ListNode(0)
        tempHead.next = head
        prev = tempHead
        
        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = curr.next
            else:  
                prev = curr
                curr = curr.next
        
        return tempHead.next
