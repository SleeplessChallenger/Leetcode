# 1. Implement Queue using Stacks
# Time & Space: O(n)
class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)
        
    def pop(self) -> int:
        return self.queue.pop(0)
        

    def peek(self) -> int:
        return self.queue[0]
        

    def empty(self) -> bool:
        return len(self.queue) == 0

# Amortized Time: O(1)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def insert(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
            # don't add return here
            # as we change `.length`
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
        return

    def pop(self):
        if not self.head:
            return None
        
        next_head = self.head.next
        curr_head = self.head
        self.head = next_head
        self.length -= 1
        
        return curr_head.value

    
class MyQueue:

    def __init__(self):
        self.queue = LinkedList()

    def push(self, x: int) -> None:
        self.queue.insert(x)
        
    def pop(self) -> int:
        return self.queue.pop()
        
    def peek(self) -> int:
        return self.queue.head.value
        
    def empty(self) -> bool:
        return self.queue.length == 0

# 2. Implement Stack using Queues
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def insert(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
        return
    
    def pop(self):
        if not self.head:
            return None
        
        old_tail = self.head
        new_tail = self.head
        while old_tail.next:
            new_tail = old_tail
            old_tail = old_tail.next
        
        self.tail = new_tail
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = 0
            self.tail = 0
        
        return old_tail.value
        

class MyStack:

    def __init__(self):
        self.stack = LinkedList()
        
    def push(self, x: int) -> None:
        self.stack.insert(x)
        
    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack.tail.value
        
    def empty(self) -> bool:
        return self.stack.length == 0


class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        
    def pop(self) -> int:
        return self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0

# 3. Keys and Rooms
   # bfs
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = [0]
        
        while len(queue) != 0:
            node = queue.pop(0)
            if node in visited:
                continue
            
            visited.add(node)
            for vertex in rooms[node]:
                queue.append(vertex)
        
        return len(visited) == len(rooms)

# 4. 01 Matrix
'''
[[0,0,0],[0,1,0],[1,1,1]]
row, col, depth = queue.pop(0)
Here row = 0, col = 1
Take (1,0) from directions

new_row = 0 + 1
new_col = 1 + 0

All checks are passed -> queue.append((new_row, new_col, 0 + 1))

'''
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        col_length = len(matrix[0])
        row_length = len(matrix)
        
        result = [[float('inf') if matrix[i][j] != 0 else 0 for j in range(col_length)]
                  for i in range(row_length)]
        
        queue = []
        visited = set()
        for i in range(row_length):
            for j in range(col_length):
                if matrix[i][j] == 0:
                    visited.add((i,j))
                    queue.append((i,j,0))
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while len(queue) != 0:
            row, col, depth = queue.pop(0)
            result[row][col] = depth
            
            for d in directions:
                new_row = row + d[0]
                new_col = col + d[1]
                
                if new_row >= 0 and new_row < row_length and\
                    new_col >= 0 and new_col < col_length and\
                    (new_row,new_col) not in visited:
                    
                    visited.add((new_row,new_col))
                    queue.append((new_row,new_col,depth+1))
        
        return result
