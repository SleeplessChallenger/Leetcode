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

# 2. Flatten a Multilevel Doubly Linked List
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    # recursive
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        tempHead = Node(None, None, head, None)
        self.traverse(tempHead, head)
        
        tempHead.next.prev = None
        return tempHead.next
    
    def traverse(self, prev, curr):
        if curr is None:
            return prev
        
        prev.next = curr
        curr.prev = prev
        
        tempNext = curr.next
        tail = self.traverse(curr, curr.child)
        
        curr.child = None
        
        return self.traverse(tail, tempNext)
    
    # iterative
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        tempHead = Node(0, None, head, None)
        stack = [head]
        prev = tempHead
        
        while len(stack) != 0:
            curr = stack.pop()
            
            curr.prev = prev
            prev.next = curr
            
            if curr.next:
                stack.append(curr.next)
            
            if curr.child:
                stack.append(curr.child)
                curr.child = None
                
            prev = curr
        
        tempHead.next.prev = None
        
        return tempHead.next

# 3. Insert into a Sorted Circular Linked List
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        '''
        Use 2 pointers and termination is when
        `prev == head`
        
        3 general cases:
        
        1. insertVal is between max and min
        => we'll insert it somewhere in the
        list
        I.e.: 3 -> 4 -> 1, insertVal = 2
        Here we'll insert between 1 and 4,
        precisely after 1 and before 3
        
        2. insertVal is bigger than max or
        smaller than min. We find tail and
        insert after it (as if < smallest,
        still it'll be after tail as head)
        
        3. list contains uniform values
        I.e. 3 -> 3 -> 3; insertVal = 0
        
        '''
        if head is None:
            var = Node(insertVal)
            var.next = var
            return var
    
        prev = head
        curr = head.next
        toInsert = False
        
        while True:
            if prev.val <= insertVal <= curr.val:
                toInsert = True
                
            # here prev is tail
            elif prev.val > curr.val:
                if insertVal >= prev.val: # if it's bigger than tail
                    toInsert = True
                elif insertVal <= curr.val: # if it's smaller than head
                    toInsert = True
                
            if toInsert:
                prev.next = Node(insertVal, curr)
                return head
            
            prev = curr
            curr = curr.next
            
            if prev == head:
                break
        
        # third case
        prev.next = Node(insertVal, curr)
        return head
