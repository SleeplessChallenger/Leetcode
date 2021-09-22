# 1. Find if Path Exists in Graph
class Solution:
	    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        queue = [start]
        graph = {}
        for vertex in range(n):
            graph[vertex] = []
        
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        visited = {start}
        
        while len(queue) != 0:
            node = queue.pop(0)
            if node == end:
                return True
            
            for vertex in graph[node]:
                if vertex not in visited:
                    visited.add(vertex)
                    queue.append(vertex)
        
        return False

# 2. All Paths From Source to Target
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        full_path = []
        queue = [[0]]
        
        while len(queue) != 0:
            curr_path = queue.pop(0)
            node = curr_path[-1]
            
            for vertex in graph[node]:
                '''
                If don't make .copy()/list()
                => further changes will affect
                another path
                '''
                temp = list(curr_path)
                temp.append(vertex)
                if vertex == len(graph) - 1:
                    full_path.append(temp)
                else:
                    queue.append(temp)

# 3. Populating Next Right Pointers in Each Node
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        
        self.traverse(root, None, None)
        return root
    
    def traverse(self, node, parent, goLeft):
        if node is None:
            return 
        
        left, right = node.left, node.right
        self.traverse(left, node, True)
        
        if parent is None:
            # for root
            node.next = None
        elif goLeft:
            node.next = parent.right
        else:
            if parent.next is None:  
                node.next = None
            else:
                node.next = parent.next.left
        
        self.traverse(right, node, False)

    # bfs
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        curr = root
        queue = [curr]
        
        while len(queue) != 0:
            size = len(queue)
            
            for i in range(size):
                node = queue.pop(0)
                
                if i < size - 1:
                    node.next = queue[0]
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return root
