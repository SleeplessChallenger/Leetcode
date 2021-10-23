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

