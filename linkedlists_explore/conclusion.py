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

# 4. Copy List with Random Pointer
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

'''
1. In recursive solution we iterate due to recursive stack
2. In iterative solution we iterate due to separate node
    that will break of the loop when it's finished
'''
class Solution:
    # Remember that we return copy of
    # .next or .random
    
    # Time: O(n) Space: O(n) Recursive
    def copyRandomList(self, head: 'Node', visited=dict()) -> 'Node':
        if head is None:
            return None
        
        # critical as in Clone Graph
        if head in visited:
            return visited[head]
        
        node = Node(head.val, None, None)
        visited[head] = node
        
        node.next = self.copyRandomList(head.next, visited)
        node.random = self.copyRandomList(head.random, visited)
        
        return node
    
    # Iterative
    def copyRandomList(self, head: 'Node', visited=dict()) -> 'Node':
        if head is None:
            return None
        
        # copy it as we need some node
        # to return from the start
        curr = head
        new_head = Node(curr.val, None, None)
        visited[curr] = new_head
        
        while curr != None:
            new_head.next = self.find_node(curr.next, visited)
            new_head.random = self.find_node(curr.random, visited)
            
            curr = curr.next
            new_head = new_head.next
            
        return visited[head]
            
    def find_node(self, node, visited):
        if node:
            if node in visited:
                return visited[node]
            else:
                temp = Node(node.val, None, None)
                visited[node] = temp
                return visited[node]            
        else:
            return None
        
    # Space: O(1)
    def copyRandomList(self, head: 'Node', visited=dict()) -> 'Node':
        if not head:
            return None
        
        curr = head
        
        while curr:
            temp = Node(curr.val, None, None)
            temp.next = curr.next
            curr.next = temp
            
            curr = temp.next
        
        curr = head

        while curr:
            # why .random.next? -> .random is a Node, but
            # it points to particular index which we didn't
            # change, hence we're to move one step further
            curr.next.random = curr.random.next if curr.random else None
            
            curr = curr.next.next
        
        curr = head
        node = curr.next
        new_head = node
        
        while curr:
            curr.next = node.next if node.next else None
            curr = curr.next if curr.next else None
            
            if curr is None:
                break
                
            node.next = curr.next
            node = node.next
            
#             curr.next = curr.next.next
#             node.next = node.next.next if node.next else None
        
#             curr = curr.next
#             node = node.next
        
        return new_head

# 5. Rotate List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        length = 1
        # here we use 1 as we want to stop
        # at last node and have it as tail,
        # but also to include it in length
        tail = head
        
        # find tail
        while tail.next:
            length += 1
            tail = tail.next
 
        offset = abs(k) % length
        # if k > length => diff between length and k
        # else: k
        
        if offset == 0:
            return head
        
        new_tail_index = length - offset if k > 0 else offset
        # if k is negative:
        # a) abs(k) < length => abs(k) % length = abs(k)
        # b) abs(k) > length => abs(k) % length = length
        
        # + keep in mind that index starts at 0
        
        count = 1
        newTail = head
        while count != new_tail_index:
            newTail = newTail.next
            count += 1

        newHead = newTail.next
        newTail.next = None
        
        tail.next = head
        return newHead
