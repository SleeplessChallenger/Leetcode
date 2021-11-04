# 1. Odd Even Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(n) Space
    '''
    1. At first count the length of LinkedList
    2. Then put values of nodes in odd/even array
    Important: start from 1 and end + 1, otherwise
        result will be wrong
    3. Start from the first node of odd and then add
        all new nodes of odd
    4. Add all nodes from even
    '''
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        odd = []
        even = []

        count = 0
        curr = head

        while curr:
            count += 1
            curr = curr.next

        curr = head
        for i in range(1, count + 1):
            if i % 2 == 0:
                even.append(curr.val)
            elif i % 2 != 0:
                odd.append(curr.val)

            curr = curr.next

        node = ListNode(odd[0])
        newHead = node
        for i in range(1, len(odd)):
            node.next = ListNode(odd[i])
            node = node.next

        for n in even:
            node.next = ListNode(n)
            node = node.next

        return newHead
    
    # O(1) Space
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # for adding to odd
        even_head = ListNode(0)
        # to move to new head
        odd_head = ListNode(0)
        even = even_head
        odd = odd_head
        isOdd = True
        
        while head:
            if isOdd:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            
            head = head.next
            isOdd = not isOdd
        
        even.next = None
        odd.next = even_head.next
        
        return odd_head.next
